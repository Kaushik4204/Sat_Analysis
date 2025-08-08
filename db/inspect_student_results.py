from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client['sat_analysis']
student_id = "65aafcf09acfd21d1abbfab5"

results = list(db['student_results'].find({'student_id': student_id}))
print(f"Found {len(results)} question responses\n")
for r in results[:3]:  # Print the first 3 responses
    pprint.pprint(r)
