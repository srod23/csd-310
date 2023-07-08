from pymongo import MongoClient

# CONNECT TO DATABASE
try:
  url = url = 'mongodb+srv://admin:admin@cluster0.rbffs5n.mongodb.net/'
  client = MongoClient(url)
  db = client.pytech;
  print('Connected to Database.')
except:
  print('Unable to connect.')


# FUNCTION FINDS ALL STUDENTS IN THE DB
def findAll():
  docs = db.students.find()

  # iterate over collection of data
  print('Find All: ')
  for doc in docs:
    print(doc)

# CALL FIND ALL FUNCTION FOR RESULTS
findAll()

# INSERT ONE
db.students.insert_one({"first_name": "Dobby", "student_id": "1010"})

# FIND ONE
db.students.find_one({"student_id": "1010"})

# DELETE ONE
db.students.delete_one({"student_id": "1010"})

# CALL FIND ALL FUNCTION FOR RESULTS
findAll()

# Close Connection
try:
  client.close()
  print("Client closed successfully.")

except:
  print("An error occurred.")
