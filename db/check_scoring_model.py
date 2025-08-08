from pymongo import MongoClient
import json
from bson import ObjectId

class ExtendedEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

client = MongoClient("mongodb://localhost:27017/")
db = client['sat_analysis']

doc = db['scoring_model'].find_one()
if doc:
    print("Scoring model document:\n")
    print(json.dumps(doc, indent=2, cls=ExtendedEncoder))
else:
    print("❌ No scoring model found in the database.")
