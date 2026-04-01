import json
import os 

FILE_DATA = "data_belanja.json"

def baca_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return[]       

def tulis_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)