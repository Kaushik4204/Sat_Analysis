from pymongo import MongoClient
from analysis.what_if_analyzer import WhatIfAnalyzer
import json
import os

def run_analysis():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sat_analysis"]

    student_ids = db["student_results"].distinct("student_id")

    for student_id in student_ids:
        analyzer = WhatIfAnalyzer(student_id, db)
        results = analyzer.analyze()

        # ✅ Ensure output directory exists before writing file
        os.makedirs("output", exist_ok=True)

        with open(f"output/{student_id}_what_if.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"Saved what-if analysis for student {student_id}")
