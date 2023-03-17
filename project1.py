import argparse
from data_manipulation import manipulateData
from classifier import Classify
from classify import PrintEvalMetrics
from file_reading import getDataset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project 1')
    parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
    parser.add_argument('dataType', nargs='?', type=str, default='Original', help='Data type; if none given, Original is default.')
    parser.add_argument('dir', nargs='?', type=str, default='BU4DFE_BND_V1.1', help='Directory;')
    args = parser.parse_args()

    ds = getDataset(args.dir)
    manipulateData(ds, args.dataType.lower())
    pred, testIndices, targets = Classify(ds, 10, args.classifier)
    PrintEvalMetrics(pred, testIndices, targets)






