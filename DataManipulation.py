import math
import numpy as np
PI = math.pi
# matrices
X_MATRIX = ([1,0,0],[0,math.cos(PI), math.sin(PI)],[0, -math.sin(PI), math.cos(PI)])
Y_MATRIX = ([math.cos(PI),0,-math.sin(PI)],[0,1, 0],[math.sin(PI), 0, math.cos(PI)])
Z_MATRIX = ([math.cos(PI), math.sin(PI), 0],[-math.sin(PI), math.cos(PI), 0],[0, 0, 1])

def Translated(data) ->list:
    x,y,z = data
    average = (x + y + z) / 3
    return [x/average, y/average, z/average]

def Rotated(data, matrix) -> list:
    x,y,z = data
    current_matrix = ([x],[y],[z])
    result = np.dot(matrix, current_matrix)
    res = [result[i][0] for i in range(3)]
    return res

def ManipulateData(data, manipulation):
    manipulation = manipulation.lower()
    matrix = {'rotatedx': X_MATRIX,
              'rotatedy': Y_MATRIX,
              'rotatedz': Z_MATRIX}
    if manipulation == "translated":
        return Translated(data)
    return Rotated(data, matrix[manipulation])

# testing
if __name__ == "__main__":
    d = [1,2,3]
    print(ManipulateData(d, "rotatedz"))