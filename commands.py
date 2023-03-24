import subprocess

cmds = [
    "python3 Project1.py TREE RotatedX ./BU4DFE_BND_V1.1 Tree-X results/Tree.txt",
    "python3 Project1.py TREE RotatedY ./BU4DFE_BND_V1.1 Tree-Y results/Tree.txt",
    "python3 Project1.py TREE RotatedZ ./BU4DFE_BND_V1.1 Tree-Z results/Tree.txt",
    "python3 Project1.py TREE Translate ./BU4DFE_BND_V1.1 Tree-Translate results/Tree.txt",
    "python3 Project1.py RF Original ./BU4DFE_BND_V1.1 RF-Original results/RF.txt",
    "python3 Project1.py RF RotatedX ./BU4DFE_BND_V1.1 RF-RotatedX results/RF.txt",
    "python3 Project1.py RF RotatedY ./BU4DFE_BND_V1.1 RF-RotatedY results/RF.txt",
    "python3 Project1.py RF RotatedZ ./BU4DFE_BND_V1.1 RF-RotatedZ results/RF.txt",
    "python3 Project1.py RF Translate ./BU4DFE_BND_V1.1 RF-Translate results/RF.txt",
    "python3 Project1.py SVM Original ./BU4DFE_BND_V1.1 SVM_Original results/SVM.txt",
    "python3 Project1.py SVM RotatedX ./BU4DFE_BND_V1.1 SVM_RotatedX results/SVM.txt",
    "python3 Project1.py SVM RotatedY ./BU4DFE_BND_V1.1 SVM_RotatedY results/SVM.txt",
    "python3 Project1.py SVM RotatedZ ./BU4DFE_BND_V1.1 SVM_RotatedZ results/SVM.txt",
    "python3 Project1.py SVM Translate ./BU4DFE_BND_V1.1 SVM_Translated results/SVM.txt"
]

for c in cmds:
    subprocess.call(c, shell=True)