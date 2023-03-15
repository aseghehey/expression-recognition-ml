import argparse
from sklearn import svm, datasets
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score
import math
import numpy as np

PI = round(2*math.acos(0.0), 3)

# matrices
X_MATRIX = ([1,0,0],[0,math.cos(PI), math.sin(PI)],[0, -math.sin(PI), math.cos(PI)])
Y_MATRIX = ([math.cos(PI),0,-math.sin(PI)],[0,1, 0],[math.sin(PI), 0, math.cos(PI)])
Z_MATRIX = ([math.cos(PI), math.sin(PI), 0],[-math.sin(PI), math.cos(PI), 0],[0, 0, 1])

#read data
def readData(filename) -> list:
    with open(filename, "r") as file:
        data = []
        for line in file:
            cur = (line[line.index(' ') + 1:].rstrip().split(' '))
            cur = list(map(lambda x: float(x), cur))
            data.append(cur)
    return data

#data type
def translated(data) ->list:
    translated = []
    for x,y,z in data:
        avg = (x + y + z)/3
        translated.append([x/avg, y/avg, z/avg])
    return translated

def rotated(data, matrix) -> list:
    rotated=[]
    for x,y,z in data:
        cur_matrix = ([x],[y],[z])
        result = np.dot(matrix, cur_matrix)
        cur = []
        for i in range(3):
            cur.append(result[i][0])
        rotated.append(cur)
    return rotated

# classifier


# main
if __name__ == "__main__":
    filename = "BU4DFE_BND_V1.1/F001/Angry/000.bnd"
    data = readData(filename)
    translated(data)
    rotation = {'RotatedX': rotated(data, X_MATRIX), 
                'RotatedY': rotated(data, Y_MATRIX),
                'RotatedZ': rotated(data, Z_MATRIX)}
    
'''
parser = argparse.ArgumentParser(description='Project 1')
parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
parser.add_argument('dataType', nargs='?', type=str, default='Original', help='Data type; if none given, Original is default.')
parser.add_argument('dir', nargs='?', type=str, default='SVM', help='Directory;')
args = parser.parse_args()

print(args.dir)
'''
