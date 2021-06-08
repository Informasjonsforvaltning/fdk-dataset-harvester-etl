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
dict_list = list(db.datasetMeta.find())
datasets = {}
for id_dict in dict_list:
    id_str = id_dict["_id"]
    datasets[id_str] = id_dict
print("Total number of extracted datasets: " + str(len(datasets)))

with open(args.outputdirectory + 'mongo_datasetMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)
