from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB server is running)
client = MongoClient('localhost', 27017)

# Create or switch to the database
db = client['user_management']

# Create or switch to the collection
collection = db['users']

# Function to add a user
def add_user(username, email):
    user = {
        "username": username,
        "email": email,
    }
    inserted_id = collection.insert_one(user).inserted_id
    print(f"User added with ID: {inserted_id}")

# Function to view all users
def view_users():
    users = collection.find()
    for user in users:
        print(user)

# Function to update a user
def update_user(user_id, updates):
    result = collection.update_one(
        {"_id": user_id},
        {"$set": updates}
    )
    if result.modified_count > 0:
        print(f"Updated user with ID {user_id}.")
    else:
        print(f"No user found with ID {user_id}.")

# Function to delete a user
def delete_user(user_id):
    result = collection.delete_one({"_id": user_id})
    if result.deleted_count > 0:
        print(f"Deleted user with ID {user_id}.")
    else:
        print(f"No user found with ID {user_id}.")

# Sample usage
if __name__ == "__main__":
    # Add users
    add_user("alice", "alice@example.com")
    add_user("bob", "bob@example.com")

    # View all users
    print("\nAll Users:")
    view_users()

    # Update a user
    update_user("60a5b4d5d5b6c2a849d4e1e9", {"email": "alice.new@example.com"})

    # View all users after update
    print("\nUsers after update:")
    view_users()

    # Delete a user
    delete_user("60a5b4d5d5b6c2a849d4e1e9")

    # View all users after deletion
    print("\nUsers after deletion:")
    view_users()

# Close the connection
client.close()
