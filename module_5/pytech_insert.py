from mongodb_test import db

#MONGODB INSERT

harry = {
  "first_name": 'Harry',
  "student_id": "1007"
}
harry_student_id = db.students.insert_one(harry).inserted_id

ron = {
  "first_name": "Ron",
  "student_id": "1008"
}
ron_student_id = db.students.insert_one(ron).inserted_id


hermoine = {
  "first_name": "Hermoine",
  "student_id": "1009"
}
hermoine_student_id = db.students.insert_one(hermoine).inserted_id

# DISPLAY RETURNED STUDENT_IDS FROM INSERT METHOD CALLS
print(harry_student_id, ron_student_id, hermoine_student_id)
