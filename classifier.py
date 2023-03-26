import time
import numpy as np
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from FileReading import GetData
from classify import PrintEvalMetrics

def Split(dataframe, nFold=10):
    """ Given a dataframe, it will split the dataframe into nFold folds, and do it so in a subject independent manner."""

    subjects = dataframe['subject'].unique() # get all the subjects
    subject_folds = np.array_split(subjects, nFold) # split the subjects into 10 folds
    split_indices = [] # list of tuples of (train, test) indices, will be returned

    for i in range(len(subject_folds)):
        test_subjects = subject_folds[i] # get current test subjects
        test = dataframe[dataframe['subject'].isin(test_subjects)] # get all data associated with current subjects
        train = dataframe[~dataframe['subject'].isin(test_subjects)] # get all data not associated with current subjects AKA Training data
        split_indices.append([train.index, test.index]) # append the indices of both train and test to the list of tuples
    return split_indices
    

def Classify(df, X, nFold=10, clf="SVM"):
    print(clf) # for debugging
    if clf == "TREE": 
        clf = DecisionTreeClassifier()
    elif clf == "RF": 
        clf = RandomForestClassifier()
    else: 
        clf = svm.SVC()

    y = df['target'].to_numpy() # get the target values as 1D array
    split_indices = Split(df, nFold) # Split data

    # used later
    pred = []
    test_indices = []
    
    for i, (train_index, test_index) in enumerate(split_indices):
        print(f"Fold {i}") # print current fold,for debugging purposes
        clf.fit(X[train_index], y[train_index]) 
        pred.append(clf.predict(X[test_index]))
        test_indices.append(test_index) # save results

    return pred, test_indices, y
