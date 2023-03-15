from sklearn import svm, datasets
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score
import argparse

def PrintEvalMetrics(pred, indices, y):
    #manually merge predictions and testing labels from each of the folds to make confusion matrix
    finalPredictions = []
    groundTruth = []
    for p in pred:
        finalPredictions.extend(p)
    for i in indices:
        groundTruth.extend(y[i])
    print(confusion_matrix(finalPredictions, groundTruth))
    print("Precision: ", precision_score(groundTruth, finalPredictions, average='macro'))
    print("Recall: ", recall_score(groundTruth, finalPredictions, average='macro'))
    print("Accuracy: " , accuracy_score(groundTruth, finalPredictions))


def CrossFoldValidation(classifier="SVM"):
    #get iris datset
    iris = datasets.load_iris()
    X = iris.data[:, :]
    y = iris.target 
    clf = None
    if classifier == "SVM":
        #default SVM 
        clf = svm.SVC()
    elif classifier == "RF":
        #default random forest
        clf = RandomForestClassifier()
    #save predictions and indices
    pred=[]
    test_indices=[]
    #4-fold cross validation
    kf = KFold(n_splits=4)
    for i, (train_index, test_index) in enumerate(kf.split(X)):
        #train classifier
        clf.fit(X[train_index], y[train_index])
        #get predictions and save
        pred.append(clf.predict(X[test_index]))
        #save current test index
        test_indices.append(test_index)
    return pred, test_indices, y

parser = argparse.ArgumentParser(description='Demo for Iris dataset classification')
parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
args = parser.parse_args()
pred, test_indices, y = CrossFoldValidation(args.classifier)
PrintEvalMetrics(pred, test_indices, y)