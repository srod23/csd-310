from pymongo import MongoClient

# CONNECT TO DATABASE
try:
  url = url = 'mongodb+srv://admin:admin@cluster0.rbffs5n.mongodb.net/'
  client = MongoClient(url)
  db = client.pytech;
  print('Connected to Database.')
except:
  print('Unable to connect.')

# FINDS ALL STUDENTS IN THE DB
def findAll():
  docs = db.students.find()

  # iterate over collection of data
  print('Find All: ')
  for doc in docs:
    print(doc)

# CALL FIND ALL FUNCTION FOR RESULTS
findAll()

# UPDATE ONE

# step 1: establish filter variable
filter = {"student_id": "1007"}

# step 2: new values
new_values = {"$set": {"last_name": "Potter!!!!!"}}

# step 3: update_one method, utilizing variables in steps 1 & 2
db.students.update_one(filter, new_values)

# FIND ONE
find_1007 = db.students.find_one({"student_id": "1007"})
print("Find One:" , find_1007)

# Close Connection
try:
  client.close()
  print("Client closed successfully.")

except:
  print("An error occurred.")
