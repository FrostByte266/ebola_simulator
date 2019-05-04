import numpy as np

def loadData(path):
    try:
        data = np.loadtxt(path, delimiter=',', skiprows=1, unpack=True)
        print(data)
        return data
    except OSError:
        print("File not found!")
        return None
