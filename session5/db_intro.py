from pymongo import MongoClient

client = MongoClient() # connect to mongodb server

db = client.get_database('d4e12') # get db name

member_collection = db.get_collection('members') # get collection name

data = {
  'name': 'Nam',
  'age': 18,
  'rela': False
}

member_collection.insert_one(data) # CREATE a record to collection

members = member_collection.find() # GET all records
for member in members:
  print(member)