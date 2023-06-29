from mongodb_test import db

harry_doc = db.students.find_one({"student_id": "1007"})
ron_doc = db.students.find_one({"student_id": "1008"})
hermoine_doc = db.students.find_one({"student_id": "1009"})

print(harry_doc, ron_doc, hermoine_doc)
