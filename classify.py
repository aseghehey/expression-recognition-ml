from FileReading import GetDataset
from sklearn import svm, datasets
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import argparse

def PrintEvalMetrics(pred, indices, y, filename="result.txt",test_name=""): # results
    #manually merge predictions and testing labels from each of the folds to make confusion matrix
    finalPredictions = []
    groundTruth = []
    for p in pred:
        finalPredictions.extend(p)
    for i in indices:
        groundTruth.extend(y[i])
    with open(filename, "a") as file:
        file.write(f"\n\n{test_name}\n{confusion_matrix(groundTruth, finalPredictions)}")
        file.write(f"\nPrecision: {precision_score(groundTruth, finalPredictions, average='macro')}")
        file.write(f"\nRecall: {recall_score(groundTruth, finalPredictions, average='macro')}")
        file.write(f"\nAccuracy: {accuracy_score(groundTruth, finalPredictions)}")


def CrossFoldValidation(classifier="SVM"):
    #get iris datset
    # iris = datasets.load_iris()
    # X = iris.data[:, :]
    # y = iris.target 
    # print(X.shape)
    X, y = GetDataset()

    clf = DecisionTreeClassifier()
    '''
    if classifier == "SVM":
        #default SVM 
        clf = svm.SVC()
    elif classifier == "RF":
        #default random forest
        clf = RandomForestClassifier()
    '''
    #save predictions and indices
    pred=[]
    test_indices=[]
    #4-fold cross validation
    kf = KFold(n_splits=10)
    
    for i, (train_index, test_index) in enumerate(kf.split(X)):
        print(train_index)
        #train classifier
        clf.fit(X[train_index], y[train_index])
        #get predictions and save
        pred.append(clf.predict(X[test_index]))
        #save current test index
        test_indices.append(test_index)

    return pred, test_indices, y

if __name__ == "__main__":
    # pred, test_indices, y =CrossFoldValidation()
    # PrintEvalMetrics(pred, test_indices, y)
    '''
    parser = argparse.ArgumentParser(description='Demo for Iris dataset classification')
    parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
    args = parser.parse_args()
    pred, test_indices, y = CrossFoldValidation(args.classifier)
    PrintEvalMetrics(pred, test_indices, y)
    '''
    iris = datasets.load_iris()
    X = iris.data[:, :]
    y = iris.target 
    print(type(iris))