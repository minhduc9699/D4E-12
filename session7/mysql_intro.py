import pymysql
from pymongo import MongoClient
from bson import ObjectId

mongo_client = MongoClient()

db = mongo_client.get_database('techkids-edu-crm-dev')
lead_collection = db.get_collection('leads')
contact_collection = db.get_collection('v2contacts')

client = pymysql.connect(
  host='localhost',
  user='root',
  password='@gmail.com',
  cursorclass=pymysql.cursors.DictCursor
)

cursor = client.cursor()

# cursor.execute('CREATE DATABASE d4e12')

cursor.execute('''
  SELECT COUNT(*) AS total, lead_id from `crm-bi-database-dev`.contact
  GROUP BY lead_id;
''')

query = {}

res = cursor.fetchall()
count = 0
for r in res:
  query['_id'] = ObjectId(r['lead_id'])
  contact_found = contact_collection.find_one(query)
  if not contact_found:
    print(r)
    count += 1
print(count)
