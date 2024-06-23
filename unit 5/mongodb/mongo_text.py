from pymongo import MongoClient 
client=MongoClient('mongodb://localhost:27017')
db=client['nithya_ganesh']
collection=db['first_collection']
data={
    "name": "Nithya Ganesh",
    "age": 19,
    "email": "nithyaganesh4343@gmail.com"
}
print(collection.insert_one(data))
print("\n")
print(collection.find_one({"name": "Nithya Ganesh"}))