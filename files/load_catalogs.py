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

with open(args.outputdirectory + 'catalogs_transformed.json') as catalogs_file:
    transformed_json = json.load(catalogs_file)

    for mongo_id in transformed_json:
        to_be_updated = transformed_json[mongo_id]
        if mongo_id == to_be_updated.get("_id"):
            print("Not updating identical ids: " + mongo_id)
        else:
            print(db.catalogMeta.insert_one(to_be_updated))
            print(db.catalogMeta.delete_one(mongo_id))
