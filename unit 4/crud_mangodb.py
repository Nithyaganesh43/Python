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
inserted_id = collection.insert_one(document).inserted_id
print(f"Inserted document with ID: {inserted_id}")

# Insert multiple documents
documents = [
    {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
    {"name": "Mike Johnson", "age": 35, "email": "mike.johnson@example.com"}
]
inserted_ids = collection.insert_many(documents).inserted_ids
print(f"Inserted documents with IDs: {inserted_ids}")

# 2. Read (Find)
# Find a single document
print("\nFinding one document:")
one_document = collection.find_one({"name": "John Doe"})
print(one_document)

# Find multiple documents
print("\nFinding multiple documents:")
all_documents = collection.find({"age": {"$gt": 20}})
for doc in all_documents:
    print(doc)

# 3. Update
# Update a single document
print("\nUpdating one document:")
result = collection.update_one(
    {"name": "John Doe"},
    {"$set": {"age": 31}}
)
print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")

# Update multiple documents
print("\nUpdating multiple documents:")
result = collection.update_many(
    {"age": {"$lt": 30}},
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
result = collection.delete_many({"status": "young"})
print(f"Deleted {result.deleted_count} document(s).")

# Close the connection
client.close()
