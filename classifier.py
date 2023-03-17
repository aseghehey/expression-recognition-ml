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

    for t, data in dataset.items():
        for _ in data:
            targets.append(t)

    expressions = np.array_split(expressions, fold)
    targets = np.array_split(targets, fold)

    if clf == "DT": clf = DecisionTreeClassifier()
    elif clf == "RF": clf = RandomForestClassifier()
    else: clf = svm.SVC()

    pred = []
    test_indices = []

    for j in range(fold): 
        print(f'Test {j}')
        for z in range(fold):
            if z == j: continue
            print(f"Fold {z}")
            clf.fit(expressions[z], targets[z])
        pred.append(clf.predict(expressions[j]))
        test_indices.append(j)
    return pred, test_indices, targets
            
def PrintEvalMetrics(pred, indices, y, file):
    #manually merge predictions and testing labels from each of the folds to make confusion matrix
    finalPredictions = []
    groundTruth = []
    for p in pred:
        finalPredictions.extend(p)
    for i in indices:
        groundTruth.extend(y[i])
    
    with open(file, "w") as res:
        res.write(f"{confusion_matrix(finalPredictions, groundTruth)}")
        res.write(f"\nPrecision: {precision_score(groundTruth, finalPredictions, average='macro')}")
        res.write(f"\nRecall: {recall_score(groundTruth, finalPredictions, average='macro')}")
        res.write(f"\nAccuracy: {accuracy_score(groundTruth, finalPredictions)}")

