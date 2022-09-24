import json


def read_categories(file):
    with open(file, "r") as f:
        data = json.load(f)

    return data
