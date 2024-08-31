import json
from pymongo import MongoClient
import geojson

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
db = client['railwap_map']  # Replace with your database name
collection = db['maps']  # Replace with your collection name

# Step 2: Load the GeoJSON file
with open("E:/temporary files\sih/backend\india-land-simplified.geojson", 'r') as file:
    geojson_data = geojson.load(file)

# Step 3: Insert GeoJSON data into MongoDB
if isinstance(geojson_data, dict):
    # Insert the data if it's a dictionary
    collection.insert_one(geojson_data)
elif isinstance(geojson_data, list):
    # Insert the data if it's a list of dictionaries
    collection.insert_many(geojson_data)

print("GeoJSON data has been successfully stored in MongoDB.")
