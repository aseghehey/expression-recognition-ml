import time
import numpy as np
from file_reading import *
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score

def Classify(dataset, fold, clf="SVM"):
    expressions = dataset['Happy'] + dataset['Sad'] + dataset['Angry'] + dataset['Fear'] + dataset['Surprise'] + dataset['Disgust']
    targets = []
    indexes = []
    i = 0
    for t, data in dataset.items():
        for _ in data:
            indexes.append(i)
            i += 1
            targets.append(t)

    expressions = np.array_split(expressions, fold)
    targets = np.array_split(targets, fold)
    indexes = np.array_split(indexes, fold)

    if clf == "DT": clf = DecisionTreeClassifier()
    elif clf == "RF": clf = RandomForestClassifier()
    else: clf = svm.SVC()

    pred = []
    test_indices = []

    print("Starting clf...")
    for j in range(fold): 
        start_time = time.perf_counter()
        for z in range(fold):
            if z == j: continue
            print(f"Fold {z}")
            clf.fit(expressions[z], targets[z])
        end_time = time.perf_counter()
        print(f"Time taken to train: {end_time - start_time}")
        pred.append(clf.predict(expressions[j]))
        test_indices.append(indexes[j])
        end_test_time = time.perf_counter()
        print(f"Time taken to test: {end_test_time - end_time}")
    return pred, test_indices, targets