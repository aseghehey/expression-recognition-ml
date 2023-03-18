import time
import numpy as np
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def Classify(X, y, ind, nFold=10, clf="SVM"):

    if clf == "TREE": 
        clf = DecisionTreeClassifier()
    elif clf == "RF": 
        clf = RandomForestClassifier()
    else: 
        clf = svm.SVC()

    pred = []
    test_indices = []

    indexes = np.array_split(ind, nFold)
    splits = []
    for i in range(nFold):
        t = []
        for j in range(nFold):
            if i == j: continue
            t.extend(indexes[j])
        splits.append((t, indexes[i]))
    
    for i, (train_index, test_index) in enumerate(splits):
        start = time.perf_counter()
        print(f"Fold {i}")
        clf.fit(X[train_index], y[train_index])
        elapsed = time.perf_counter() - start
        print(f"Time: {elapsed}")
        pred.append(clf.predict(X[test_index]))
        test_indices.append(test_index)

    return pred, test_indices, y