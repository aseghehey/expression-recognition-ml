import argparse
from DataManipulation import ManipulateData
from Classifier import Classify
from classify import PrintEvalMetrics
from FileReading import GetData

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project 1')
    # get arguments from CLI
    parser.add_argument('classifier', nargs='?', type=str, default='SVM', help='Classifier type; if none given, SVM is default.')
    parser.add_argument('dataType', nargs='?', type=str, default='Original', help='Data type; if none given, Original is default.')
    parser.add_argument('dir', nargs='?', type=str, default='BU4DFE_BND_V1.1', help='Directory;')
    args = parser.parse_args()

    df, data = GetData(path=args.dir, manipulation=args.dataType)
    pred, testIndices, targets = Classify(df, data, clf=args.classifier)
    PrintEvalMetrics(pred, testIndices, targets)