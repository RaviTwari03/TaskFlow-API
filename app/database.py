from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://rt9593878_db_user:<JOnykOk3SERWwK1q>@taskflowapicluster0.9nbp6wq.mongodb.net/?appName=TaskFlowAPICluster0")

client = MongoClient(MONGO_URL)
db = client["taskflow"]
users_collection = db["users"]
products_collection = db["products"]