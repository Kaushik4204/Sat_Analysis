import os
import json
from datetime import datetime
from pymongo import MongoClient
from analysis.what_if_analyzer import WhatIfAnalyzer

client = MongoClient("mongodb://localhost:27017/")
db = client['sat_analysis']

# Replace with actual student IDs
student_ids = [
    "65aafd6d9acfd21d1abbfaae",
    "65aafcf09acfd21d1abbfab5"
]

os.makedirs('output', exist_ok=True)

for student_id in student_ids:
    analyzer = WhatIfAnalyzer(student_id, db)
    result = analyzer.analyze()

    filename = f"output/{student_id}_whatif_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Saved analysis for {student_id} to {filename}")
