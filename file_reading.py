import os
from collections import defaultdict

def readData(filename, data) -> None:
    """ Given a file and array, reads contents of file and appends to array as floats"""
    with open(filename, "r") as file:
        for line in file:
            cur = (line[line.index(' ') + 1:].rstrip().split(' '))
            cur = list(map(lambda x: float(x), cur))
            data.append(cur)

# [46.636056, 14.644247, -93.946304]
def getDataset(path='BU4DFE_BND_V1.1'):
    dataset = defaultdict(list)
    dir = os.walk(path)
    for folder_path, _, _ in dir:
        cur_emotion = folder_path.split('/')[-1]
        # only interested in expression directory, ignore others
        if cur_emotion not in {'Happy', 'Sad', 'Angry', 'Fear', 'Surprise', 'Disgust'}:
            continue
        files = os.listdir(folder_path) # gets list of all the files within the expression directory
        for file in files: # go through each file and add it to dataset
            # do not want to assume that directory only contains correct files, so checking
            extension_checker = file[file.index('.'):] in {'.bnd','.landmark'}
            if not extension_checker: continue 
            filepath = folder_path + '/' + file # would be something like BU4DFE_BND_V1.1/F001/Angry/000.bnd
            readData(filename=filepath, data=dataset[cur_emotion])
    return dataset