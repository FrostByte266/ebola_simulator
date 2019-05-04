import numpy as np
import json

def loadData(path):
    try:
        if path[-5:] != ".json":
            raise ValueError
        data = json.loads(open(path, 'r').read())
        return data
    except OSError:
        print("File not found!")
        return None
    except ValueError:
        print("File extension invalid, are you loading a JSON file?")
        return None
