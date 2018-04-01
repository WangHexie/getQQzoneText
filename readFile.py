import os
import pandas as pd
from IPython import display
import numpy as np


def getFileList(path="D:\programming\sentence\\"):
    dirs = os.listdir(path)
    return path, dirs


def mod(chara, QQ):  # 模式判断，若为空则选择全部
    if QQ == None:
        return 1
    else:
        return chara == QQ


def getSentences(QQ=None):
    path, fileList = getFileList()
    for i in fileList:
        if mod(i.split('_')[0], QQ):  # 模式判断，若为空则选择全部
            with open(path + i, "r") as f:
                k = f.read()
                yield k


def getAllMultyClass():  # 未处理，class 为QQ号
    path, fileList = getFileList()
    sentences = []
    classes = []
    for i in fileList:
        with open(path + i, "r") as f:
            k = f.read()
            if k != "" and k != "发表图片":
                sentences.append(k)
                classes.append(i.split('_')[0])
                # print(k)
    return pd.DataFrame({'sentence': pd.Series(sentences), 'class': pd.Series(classes)})


def getAllTwoClasses(QQ):
    path, fileList = getFileList()
    sentences = []
    classes = []
    for i in fileList:
        with open(path + i, "r") as f:
            k = f.read()
            if k != "" and k != "发表图片":
                sentences.append(k)
                if i.split('_')[0] == QQ:
                    classes.append(1)
                else:
                    classes.append(0)
    FCDF = pd.DataFrame({'sentence': pd.Series(sentences), 'class': pd.Series(classes)})
    FCDF = FCDF.reindex(
        np.random.permutation(FCDF.index))
    return FCDF


def saveDic(dic, path="D:\programming\MLModel\dic.txt"):
    with open(path, "w") as f:
        f.write(str(dic))
        return 1


def saveList(list, path="D:\programming\MLModel\List.txt"):
    with open(path, "w") as f:
        f.write(str(list))
        return 1


def loadList(path="D:\programming\MLModel\List.txt"):
    with open(path, "r") as f:
        list = f.read()
        return eval(list)


def loadDic(path="D:\programming\MLModel\dic.txt"):
    with open(path, "r") as f:
        dic = f.read()
    return eval(dic)


if __name__ == '__main__':
    k = 0
    for _ in getSentences():
        k += 1
    print(k)
