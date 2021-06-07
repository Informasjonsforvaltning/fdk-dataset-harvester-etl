import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
new_base_uri = os.environ['FDK_REGISTRATION_BASE_URI']


def transform(inputfile, inputfile2):

    catalogs = openfile(inputfile)
    catalogs_meta = openfile(inputfile2)
    transformed_catalogs = {}
    print("Total number of extracted catalogs: " + str(len(catalogs)))
    for catalog_key in catalogs:
        old_id = catalogs[catalog_key].get("uri")
        new_id = str_split(old_id)
        to_be_transformed = catalogs_meta.get(old_id)
        if to_be_transformed:
            transformed = transform_catalog(to_be_transformed, new_id)
            transformed_catalogs[old_id] = transformed
    return transformed_catalogs


def transform_catalog(to_be_transformed, new_id):
    transformed = to_be_transformed
    transformed["_id"] = new_id
    return transformed


def str_split(uri):
    str_spl = uri.split('catalogs/')
    return new_base_uri + '/catalogs/' + str_spl[-1]


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_catalogs.json"
inputfileName2 = args.outputdirectory + "mongo_catalogMeta.json"
outputfileName = args.outputdirectory + "catalogs_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileName2), outfile, ensure_ascii=False, indent=4)
