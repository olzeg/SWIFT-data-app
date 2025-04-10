from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

df = pd.read_csv("SWIFT_CODES.csv")

load_dotenv()

connection_string = os.getenv("mongo_uri")

client = MongoClient(connection_string) #connecting to MongoDB
db = client["swift_project"]
collection = db["swift_codes"]

records = df.to_dict(orient='records')
collection.insert_many(records)

collection.create_index("swift_code")
collection.create_index("country_code")