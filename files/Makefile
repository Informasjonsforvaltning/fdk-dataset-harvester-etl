.PHONY: test
all: extract transform load

extract:
	echo "Extracting...."
	python3 ./extract_datasets.py -o ./tmp/

transform:
	echo "Transforming...."
	python3 -u ./transform_datasets.py -o ./tmp/

load_datasets:
	echo "Loading...."
	python3 ./load_datasets.py -o ./tmp/

load_catalogs:
	echo "Loading...."
	python3 ./load_catalogs.py -o ./tmp/

clean:
	rm ./tmp/*.json
