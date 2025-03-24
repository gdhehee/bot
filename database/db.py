
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")  # Set in .env file
client = pymongo.MongoClient(MONGO_URI)
db = client['ultimate_bot']  # The database name
warnings_collection = db['warnings']
invites_collection = db['invites']
usage_collection = db['usage']

# Create necessary indexes for collections
warnings_collection.create_index([('user_id', pymongo.ASCENDING), ('guild_id', pymongo.ASCENDING)], unique=True)
invites_collection.create_index([('user_id', pymongo.ASCENDING), ('guild_id', pymongo.ASCENDING)], unique=True)
usage_collection.create_index([('user_id', pymongo.ASCENDING), ('date', pymongo.ASCENDING)], unique=True)

# Function to get the MongoDB collections
def get_collections():
    return warnings_collection, invites_collection, usage_collection
