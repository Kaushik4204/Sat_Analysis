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


---

## ⚙️ Setup Instructions

### 1. 🔧 Prerequisites

- Python 3.8+
- [MongoDB](https://www.mongodb.com/try/download/community) installed locally
- Git installed

### 2. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 3. 🗃️ Import data into MongoDB

# Start MongoDB service (if not running)
```bash
mongod --dbpath /path/to/your/mongodb/data
```

# Then run:
```bash
python db/insert_sample_data.py
```

This will populate:

sat_analysis.student_results with student attempts

sat_analysis.scoring_model with the SAT scoring table

### 4. Run the analysis
```bash
python main.py
```
This generates what-if analysis JSONs per student in the output/ folder.

## Testing (Optional)
To test logic for multiple students:
```bash
python tests/test_students.py
```

### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss the change.

### 🙌 Acknowledgements
This project was built as part of a technical assessment by HighScores.ai
