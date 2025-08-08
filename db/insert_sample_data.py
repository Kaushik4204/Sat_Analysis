from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['sat_analysis']

student_id = "65aafcf09acfd21d1abbfab5"  # Replace or loop over multiple students if needed

sample_data = [
    {
        "student_id": student_id,
        "question_id": "Q1",
        "correct": 0,
        "subject": {"name": "Math"},
        "section": "adaptive",
        "topic": {"name": "Algebra"},
        "unit": {"name": "Equations"}
    },
    {
        "student_id": student_id,
        "question_id": "Q2",
        "correct": 0,
        "subject": {"name": "Math"},
        "section": "static",
        "topic": {"name": "Geometry"},
        "unit": {"name": "Angles"}
    },
    {
        "student_id": student_id,
        "question_id": "Q3",
        "correct": 1,
        "subject": {"name": "English"},
        "section": "adaptive",
        "topic": {"name": "Reading Comprehension"},
        "unit": {"name": "Main Ideas"}
    },
    {
        "student_id": student_id,
        "question_id": "Q4",
        "correct": 0,
        "subject": {"name": "English"},
        "section": "static",
        "topic": {"name": "Grammar"},
        "unit": {"name": "Tenses"}
    }
]

db['student_results'].delete_many({'student_id': student_id})  # Clean old test data
db['student_results'].insert_many(sample_data)
print("✅ Sample data inserted.")
