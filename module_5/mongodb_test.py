from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.rbffs5n.mongodb.net/'

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())
