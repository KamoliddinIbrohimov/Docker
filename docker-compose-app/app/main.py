from pymongo import MongoClient
from pprint import pprint


MONGO_URL = "mongodb://mongo:27016"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = client.admin.command("listDatabases")
pprint(dbs_list)

print("End")
