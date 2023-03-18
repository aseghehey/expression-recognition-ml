import argparse
from DataManipulation import ManipulateData
from Classifier import Classify
from classify import PrintEvalMetrics
from FileReading import GetDataset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project 1')
    parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
    parser.add_argument('dataType', nargs='?', type=str, default='Original', help='Data type; if none given, Original is default.')
    parser.add_argument('dir', nargs='?', type=str, default='BU4DFE_BND_V1.1', help='Directory;')
    parser.add_argument('testName', nargs='?', type=str, default='Test', help='File;')
    args = parser.parse_args()

    data, targets, indices = GetDataset(args.dir, args.dataType)
    pred, testIndices, targets = Classify(data, targets, indices, 10, args.classifier)
    PrintEvalMetrics(pred, testIndices, targets, test_name=args.testName)






