import argparse
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score
from data_manipulation import manipulateData
from classifier import Classify, PrintEvalMetrics
from file_reading import getDataset
# classifier


# main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project 1')
    parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
    parser.add_argument('dataType', nargs='?', type=str, default='Original', help='Data type; if none given, Original is default.')
    parser.add_argument('dir', nargs='?', type=str, default='BU4DFE_BND_V1.1', help='Directory;')
    args = parser.parse_args()

    print(args.classifier, args.dataType, args.dir)

    # ds = getDataset()
    # pred, indices, targets = Classify(ds, 10, "")







