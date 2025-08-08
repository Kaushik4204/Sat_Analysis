# SAT What-If Score Analysis Tool 🎓

## 📘 Overview

This project is designed to simulate **what-if analysis** on SAT diagnostic results to help students identify which incorrect responses, if answered correctly, would most improve their scores.

We implement scoring logic using a **section-adaptive** SAT model with student result data and scoring maps. The output includes detailed score improvement recommendations per question and topic.

---

## 🗂 Project Structure

SAT_Analysis/

│

├── analysis/ # Core logic for adaptive analysis

│ ├── adaptive_threshold.py

│ └── what_if_analyzer.py

│

├── data/ # Input data files (student results & scoring model)

│ ├── 66fece285a916f0bb5aea9c5user_attempt_v3.json

│ ├── 67f2aae2c084263d16dbe462user_attempt_v2.json

│ └── scoring_DSAT_v2.json

│

├── db/ # MongoDB helper scripts

│ ├── check_scoring_model.py

│ ├── insert_sample_data.py

│ └── inspect_student_results.py

│

├── output/ # Final JSON output from what-if analysis

│ ├── <student_id>whatif<timestamp>.json

│

├── tests/ # Optional test suite

│ └── test_students.py

│

├── utils/ # Scoring and helper functions

│ └── scorer.py

│

├── main.py # Main entry point

├── requirements.txt # Python dependencies

└── README.md 
