from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("mongodb+srv://rt9593878_db_user:<JOnykOk3SERWwK1q>@taskflowapicluster0.9nbp6wq.mongodb.net/?appName=TaskFlowAPICluster0"))
db = client["taskflow"]
collection = db["tasks"]