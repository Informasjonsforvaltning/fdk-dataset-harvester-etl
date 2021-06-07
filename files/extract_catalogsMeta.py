import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection.datasetHarvester
dict_list = list(db.catalogMeta.find())
catalogs = {}
for id_dict in dict_list:
    id_str = id_dict["_id"]
    catalogs[id_str] = id_dict
print("Total number of extracted catalogs: " + str(len(catalogs)))

with open(args.outputdirectory + 'mongo_catalogMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)