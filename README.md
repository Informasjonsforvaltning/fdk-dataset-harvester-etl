# fdk-dataset-harvester-etl
ETL type utilities related to our dataset harvester

A successful ETL requires the following sequence:

1. Update fdkID (ETL with TO_BE_UPDATED = fdkID)
2. remove turtle data from mongodb for dataset-harvester
3. restart harvester
4. update dates (T+L with TO_BE_UPDATE = dates)
5. post to harvester update/meta

Change env variable: export TO_BE_UPDATED = "value"

Set workflow files to trigger on current branch name.
Github pages should also be set to branch name, if changes has been made to it.