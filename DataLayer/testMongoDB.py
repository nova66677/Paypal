from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create a database
db_name = "myDatabase"
db = client[db_name]

# Create a collection
collection_name = "UserTable"
collection = db[collection_name]

# Insert a sample document
sample_document = {"email": "echopin91@gmail.com", "password_hash": "7168468768484268728", "profile_data": {"first_name":"Eliott", "last_name":"Chopin", "kyc_status":"Verified", "created_at:":"24/01/2025 17:56"}}
collection.insert_one(sample_document)

print(f"Database '{db_name}' and collection '{collection_name}' created successfully.")
print("Sample document inserted:", sample_document)
