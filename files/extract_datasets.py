import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")

# Old datasets
db = connection.datasetHarvester
dict_list = list(db.dataset.find())
datasets = {}
for id_dict in dict_list:
    dataset = {}
    id_str = id_dict["_id"]
    fdkId_str = id_dict["fdkId"]
    issued_str = id_dict["issued"]
    modified_str = id_dict["modified"]
    dataset["_id"] = id_str
    dataset["fdkId"] = fdkId_str
    dataset["issued"] = issued_str
    dataset["modified"] = modified_str
    datasets[id_str] = dataset


with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)

# New datasets
db = connection.datasetHarvester
dict_list = list(db.datasetMeta.find({}, {"_id": 1}))
datasets = []
for id_dict in dict_list:
    datasets.append(id_dict["_id"])

with open(args.outputdirectory + 'mongo_datasetsMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataset, outfile, ensure_ascii=False, indent=4)

# Old catalogs
db = connection.datasetHarvester
dict_list = list(db.catalog.find())
catalogs = []
for id_dict in dict_list:
    catalog = {}
    id_str = id_dict["_id"]
    fdkId_str = id_dict["fdkId"]
    issued_str = id_dict["issued"]
    modified_str = id_dict["modified"]
    catalog["_id"] = id_str
    catalog["fdkId"] = fdkId_str
    catalog["issued"] = issued_str
    catalog["modified"] = modified_str
    catalogs[id_str] = catalog

with open(args.outputdirectory + 'mongo_catalogs.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)

# New catalogs
db = connection.datasetHarvester
dict_list = list(db.catalogMeta.find({}, {"_id": 1}))
catalogs = []
for id_dict in dict_list:
    catalogs.append(id_dict["_id"])

with open(args.outputdirectory + 'mongo_catalogsMeta.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)