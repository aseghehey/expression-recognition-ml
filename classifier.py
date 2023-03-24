import time
import numpy as np
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from FileReading import GetData
from classify import PrintEvalMetrics

def Split(dataframe, nFold=10):
    subjects = dataframe['subject'].unique()
    subject_folds = np.array_split(subjects, nFold)
    
    split_indices = []
    for i in range(len(subject_folds)):
        test_subjects = subject_folds[i]
        test = dataframe[dataframe['subject'].isin(test_subjects)]
        train = dataframe[~dataframe['subject'].isin(test_subjects)]
        split_indices.append([train.index, test.index])
    return split_indices
    

def Classify(df, X, nFold=10, clf="SVM"):

    if clf == "TREE": 
        clf = DecisionTreeClassifier()
    elif clf == "RF": 
        clf = RandomForestClassifier()
    else: 
        clf = svm.LinearSVC(dual=False)

    y = df['target'].to_numpy()
    split_indices = Split(df, nFold)

    pred = []
    test_indices = []
    
    for i, (train_index, test_index) in enumerate(split_indices):
        print(f"Fold {i}")
        start = time.perf_counter()
        clf.fit(X[train_index], y[train_index])
        print(f"Elapsed train: {time.perf_counter() - start}")
        pred.append(clf.predict(X[test_index]))
        test_indices.append(test_index)

    return pred, test_indices, y
