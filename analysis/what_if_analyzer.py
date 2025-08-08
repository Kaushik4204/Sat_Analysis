from collections import defaultdict
from copy import deepcopy


class WhatIfAnalyzer:
    def __init__(self, student_id, db, adaptive_threshold=0.5):
        self.student_id = student_id
        self.db = db
        self.adaptive_threshold = adaptive_threshold
        self.raw_data = list(db['student_results'].find({'student_id': student_id}))
        self.scoring_map = self._load_scoring_map()

    def _is_correct(self, q):
        """Safely check if a question is marked correct."""
        return str(q.get('correct', 0)) == '1'

    def _load_scoring_map(self):
        doc = self.db['scoring_model'].find_one()
        if not doc:
            print("⚠️ Scoring model document not found.")
            return {}

        flat_map = {}
        for k, v in doc.items():
            if k == '_id':
                continue
            flat_map[k.lower().strip()] = {str(score): val for score, val in v.items()}

        return flat_map

    def _get_sections(self):
        math = []
        english = []
        for q in self.raw_data:
            subject = q['subject']['name'].lower().strip()
            if subject == 'math':
                math.append(q)
            else:
                english.append(q)
        return math, english

    def _split_modules(self, section_data):
        m1 = [q for q in section_data if q['section'].lower().strip() == 'static']
        m2 = [q for q in section_data if q['section'].lower().strip() == 'adaptive']
        return m1, m2

    def _determine_adaptive_level(self, m1_questions):
        if not m1_questions:
            return 'easy'
        correct = sum(1 for q in m1_questions if self._is_correct(q))
        return 'hard' if correct / len(m1_questions) >= self.adaptive_threshold else 'easy'

    def _calculate_raw_score(self, section_data):
        return sum(1 for q in section_data if self._is_correct(q))

    def _get_scaled_score(self, section, raw_score, difficulty):
        subject_key_map = {
            "math": "math",
            "english": "reading and writing"
        }
        normalized_subject = subject_key_map.get(section.lower(), section.lower())
        key = f"{normalized_subject}_{difficulty.lower()}"
        table = self.scoring_map.get(key)

        if not table:
            print(f"⚠️ Warning: Scoring key '{key}' not found in scoring map.")
            return 0

        return table.get(str(raw_score), 0)

    def _run_section_what_if(self, section_name, section_data):
        m1, _ = self._split_modules(section_data)
        raw_score = self._calculate_raw_score(section_data)
        difficulty = self._determine_adaptive_level(m1)
        scaled_score = self._get_scaled_score(section_name, raw_score, difficulty)

        what_if_results = []

        for i, q in enumerate(section_data):
            if self._is_correct(q):
                continue

            modified_section = deepcopy(section_data)
            modified_section[i]['correct'] = 1  # simulate changing this one to correct

            new_m1, _ = self._split_modules(modified_section)
            new_difficulty = self._determine_adaptive_level(new_m1)
            new_raw = self._calculate_raw_score(modified_section)
            new_scaled = self._get_scaled_score(section_name, new_raw, new_difficulty)

            delta = new_scaled - scaled_score

            what_if_results.append({
                'question_id': q.get('question_id'),
                'section': section_name,
                'module': q.get('section'),
                'topic': q.get('topic', {}).get('name', 'Unknown'),
                'unit': q.get('unit', {}).get('name', 'Unknown'),
                'raw_score_change': 1,
                'scaled_score_change': delta,
                'old_scaled': scaled_score,
                'new_scaled': new_scaled,
                'adaptive_change': difficulty != new_difficulty,
                'original_difficulty': difficulty,
                'new_difficulty': new_difficulty,
                'cascade': difficulty != new_difficulty
            })

        return scaled_score, what_if_results

    def analyze(self):
        math, english = self._get_sections()
        math_score, math_impact = self._run_section_what_if("math", math)
        eng_score, eng_impact = self._run_section_what_if("english", english)

        all_impacts = sorted(math_impact + eng_impact, key=lambda x: -x['scaled_score_change'])

        topic_impact = defaultdict(int)
        for item in all_impacts:
            topic_impact[item['topic']] += item['scaled_score_change']

        top_topics = sorted(topic_impact.items(), key=lambda x: -x[1])[:5]

        return {
            'student_id': self.student_id,
            'current_scores': {
                'math': math_score,
                'english': eng_score,
                'total': math_score + eng_score
            },
            'recommendation_summary': {
                'total_possible_gain': sum(x['scaled_score_change'] for x in all_impacts),
                'top_topics_by_impact': top_topics
            },
            'recommendations': all_impacts
        }
