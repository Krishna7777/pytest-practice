import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DATA_DIR = BASE_DIR.joinpath('testdata')

def get_json_from_file(filepath, filename):
    file_path = TEST_DATA_DIR.joinpath(filepath, filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def read_data_from_csv_file(filepath, filename):
    file_path = TEST_DATA_DIR.joinpath(filepath, filename)
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        lines = list(reader)
    return lines


if __name__ == '__main__':
    json = get_json_from_file('pet_api_json', 'create_pet.json')
    print(json)

