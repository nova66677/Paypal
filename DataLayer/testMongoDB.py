from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create a database
db_name = "myDatabase"
db = client[db_name]

# Create a collection
collection_name = "myCollection"
collection = db[collection_name]

# Insert a sample document
sample_document = {"name": "John Doe", "age": 30, "city": "New York"}
collection.insert_one(sample_document)

print(f"Database '{db_name}' and collection '{collection_name}' created successfully.")
print("Sample document inserted:", sample_document)
