from pymongo import MongoClient
import json
client = MongoClient('mongodb://localhost:27017/')
db = client[<database_name>]
collection = db[<collection_name>]
cursor = collection.find()
with open('<output_file.json>', 'w') as f:
    for document in cursor:
        json.dump(document, f)
        f.write('\n')
