from mongodb_test import db


# FIND({})
docs = db.students.find({})
print('Find All: ')
for doc in docs:
  print(doc)

#FIND.ONE({})
harry_doc = db.students.find_one({"student_id": "1007"})
print('Find One: ', harry_doc)

ron_doc = db.students.find_one({"student_id": "1008"})
# print(ron_doc)

hermoine_doc = db.students.find_one({"student_id": "1009"})
# print(hermoine_doc)
