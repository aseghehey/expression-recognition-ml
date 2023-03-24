import math
import numpy as np

def Translate(arr):
    average = sum(arr)/len(arr)
    for i in range(len(arr)):
        arr[i] -= average
    return arr

def Rotate(arr, idx) -> list:
    """ idx {0:x, 1:y, 2: z}"""
    for i in range(len(arr)):
        if i == idx: continue
        arr[i] *= -1
    return arr    

def ManipulateData(data, manipulation):
    manipulation = manipulation.lower()
    if manipulation == "original":
        return data
    axis_index = {'rotatedx': 0,
                  'rotatedy': 1,
                  'rotatedz': 2}
    if  manipulation == "translate":
        return Translate(data)
    return Rotate(data, axis_index[manipulation])
