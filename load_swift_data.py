from pymongo import MongoClient
import pandas as pd

df = pd.read_csv("SWIFT_CODES.csv")

connection_string = "mongodb+srv://olgazegzda:<>@swift-codes.tfrawb6.mongodb.net/?retryWrites=true&w=majority&appName=SWIFT-codes"

client = MongoClient(connection_string) #connecting to MongoDB
db = client["swift_project"]
collection = db["swift_codes"]

records = df.to_dict(orient='records')
collection.insert_many(records)

collection.create_index("swift_code")
collection.create_index("country_code")