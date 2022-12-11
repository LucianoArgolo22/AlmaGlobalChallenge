import json

def open_json(file, mode="r", dictionary = None):
    with open(file, mode, encoding="UTF-8") as file:
        if mode == "r":
            return json.loads(file.read())
        else:
            return json.dump(dictionary, file, indent = 4)
