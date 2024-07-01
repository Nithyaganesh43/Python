from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB server is running)
client = MongoClient('localhost', 27017)

# Create or switch to the database
db = client['test_database']

# Create or switch to the collection
collection = db['test_collection']

# 1. Create (Insert)
# Insert a single document
document = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}
collection.insert_one(document)
print("Inserted document ")

# Insert multiple documents
documents = [
    {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
    {"name": "Mike Johnson", "age": 35, "email": "mike.johnson@example.com"}
]
collection.insert_many(documents)
print(f"Inserted documents ")

# 2. Read (Find)
# Find a single document
print("\nFinding one document:")
one_document = collection.find_one({"name": "John Doe"})
print(one_document)

# Find multiple documents
print("\nFinding multiple documents:")
all_documents = collection.find({})
for doc in all_documents:
    print(doc)

# 3. Update
# Update a single document
print("\nUpdating one document:")
result = collection.update_one(
    {"name": "John Doe"},{"$set": {"age": 30}}
)
print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")

# Update multiple documents
print("\nUpdating multiple documents:")
result = collection.update_many(
    {"age": 30},
    {"$set": {"status": "young"}}
)
print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")

# 4. Delete
# Delete a single document
print("\nDeleting one document:")
result = collection.delete_one({"name": "Mike Johnson"})
print(f"Deleted {result.deleted_count} document(s).")

# Delete multiple documents
print("\nDeleting multiple documents:")
result = collection.delete_many({"age":30})
print(f"Deleted {result.deleted_count} document(s).")




print("\nDeleting all datas:")
collection.delete_many({})


print("\nDeleting collection:")
collection.drop()



print("\nDeleting data base:")
client.drop_database("test_database")
# Close the connection
client.close()
