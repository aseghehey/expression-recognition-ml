import numpy as np

DIM = 3
def Translate(arr):
    X_sum = 0
    Y_sum = 0
    Z_sum = 0
    total = len(arr)/DIM
    get_it = arr[:DIM]
    # not executing:
    for i in range(0, len(arr), DIM):
        X_sum += arr[i]
        Y_sum += arr[i + 1]
        Z_sum += arr[i + 2]

    X_avg = X_sum / total
    Y_avg = Y_sum / total
    Z_avg = Z_sum / total

    for i in range(0, len(arr), DIM):
        arr[i] -= X_avg
        arr[i + 1] -= Y_avg
        arr[i + 2] -= Z_avg

def Rotate(arr, idx) -> list:
    """ Given array, rotate it over the X-, Y-, or Z-axis. Use idx to specify which axis to rotate over, where 0 is X, 1 is Y, and 2 is Z."""
    for i in range(0, len(arr), DIM):
        if (idx == 0):
            arr[i + 1] *= -1
            arr[i + 2] *= -1
        elif (idx == 1):
            arr[i] *= -1
            arr[i + 2] *= -1
        else:
            arr[i] *= -1
            arr[i + 1] *= -1

def ManipulateData(data, manipulation):
    """ Connects the Translate Rotate functions together"""
    axis_index = {'rotatedx': 0,
                  'rotatedy': 1,
                  'rotatedz': 2}
    if  manipulation == "translated":
        Translate(data)
        return
    Rotate(data, axis_index[manipulation])
