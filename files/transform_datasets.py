import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
update_dates = os.environ["TO_BE_UPDATED"] == 'dates'


def transform(inputfile, inputfile_meta, failed_path):

    datasets = openfile(inputfile)
    datasets_meta = openfile(inputfile_meta)

    transformed = {}
    failed = {}

    for dataset_key in datasets:
        if dataset_key not in datasets_meta:
            failed[dataset_key] = (datasets[dataset_key]["_id"])
        else:
            transformed[datasets[dataset_key]["_id"]] = fields_to_change(datasets[dataset_key])

    with open(failed_path, 'w', encoding="utf-8") as failed_file:
        json.dump(failed, failed_file, ensure_ascii=False, indent=4)
    return transformed


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def fields_to_change(dataset):
    if update_dates is True:
        return {"issued": dataset["issued"],
                "modified": dataset["modified"]}
    else:
        return {"fdkId": dataset["fdkId"]}


inputfileName = args.outputdirectory + "mongo_datasets.json"
inputfileNameMeta = args.outputdirectory + "mongo_datasetsMeta.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"
failedfileName = args.outputdirectory + "failed_transform_datasets.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta, failedfileName), outfile, ensure_ascii=False, indent=4)

# Catalogs
inputfileName = args.outputdirectory + "mongo_catalogs.json"
inputfileNameMeta = args.outputdirectory + "mongo_catalogsMeta.json"
outputfileName = args.outputdirectory + "catalogs_transformed.json"
failedfileName = args.outputdirectory + "failed_transform_catalogs.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileNameMeta, failedfileName), outfile, ensure_ascii=False, indent=4)