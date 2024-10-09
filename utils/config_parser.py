import configparser
from pathlib import Path

config_dir = "config"
config_file = "petsqa.ini"

config_parser = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
config_file_path = BASE_DIR.joinpath(config_dir).joinpath(config_file)
config_parser.read(config_file_path)

def get_pet_app_url():
    return config_parser['pet']['url']

if __name__ == "__main__":
    print(get_pet_app_url())