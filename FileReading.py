import os
import numpy as np
from DataManipulation import ManipulateData

def ReadData(filename, manipulator):
    """ Given a file and array, reads contents of file and appends to array as floats"""
    temp = []
    with open(filename, "r") as file:
        for line in file:
            cur = (line[line.index(' ') + 1:].rstrip().split(' '))
            cur = list(map(lambda x: float(x), cur))
            if manipulator != "original":
                cur = ManipulateData(cur, manipulator)
            for v in cur: temp.append(v)
    return temp

def GetDataset(path='BU4DFE_BND_V1.1', manipulation="original"):
    data = []
    target = []
    # to map emotion to a number
    map_emotion = {'Happy':0, 'Sad':1, 'Angry':2, 'Fear':3, 'Surprise':4, 'Disgust':5}

    dir = os.walk(path)
    for folder_path, _, _ in dir:
        cur_emotion = folder_path.split('/')[-1]
        # only interested in expression directory, ignore others
        if cur_emotion not in {'Happy', 'Sad', 'Angry', 'Fear', 'Surprise', 'Disgust'}:
            continue
        files = os.listdir(folder_path) # gets list of all the files within the expression directory
        for file in files: # go through each file and add it to dataset
            # do not want to assume that directory only contains correct files, so checking
            extension_checker = file[file.index('.'):] == ".bnd"
            if not extension_checker: continue 
            filepath = folder_path + '/' + file # would be something like BU4DFE_BND_V1.1/F001/Angry/000.bnd
            target.append(map_emotion[cur_emotion])
            data.append(ReadData(filename=filepath, manipulator=manipulation))

    target = np.array(target)
    data = np.array(data)
    indices = [i for i in range(len(data))] # useful for train and test indices
    indices = np.array(indices)

    return data, target, indices

if __name__ == "__main__":
    d, t, indices = GetDataset(manipulation="translate")