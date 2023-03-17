import math
import numpy as np

PI = math.pi
# matrices
X_MATRIX = ([1,0,0],[0,math.cos(PI), math.sin(PI)],[0, -math.sin(PI), math.cos(PI)])
Y_MATRIX = ([math.cos(PI),0,-math.sin(PI)],[0,1, 0],[math.sin(PI), 0, math.cos(PI)])
Z_MATRIX = ([math.cos(PI), math.sin(PI), 0],[-math.sin(PI), math.cos(PI), 0],[0, 0, 1])

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

def manipulateData(data, manipulation):
    manipulation = manipulation.lower()
    if manipulation == "original": return
    translation_flag = manipulation == 'translate'
    matrix = {'rotatedx': X_MATRIX,
              'rotatedy': Y_MATRIX,
              'rotatedz': Z_MATRIX}
    for key in data.keys():
        if translation_flag:
            data[key] = translated(data[key])
            continue
        data[key] = rotated(data[key], matrix[manipulation])
