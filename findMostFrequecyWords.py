from readFile import *
from getWords import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def findMostFrequencyWords(QQ=None):
    dict = {}
    wordList = []
    frequencyList = []
    wordQuantity = 0
    histograms_x = np.array([])
    histograms_y = np.array([])
    seg = 30
    thu1 = thulac.thulac(user_dict=None, model_path=None, T2S=False, seg_only=True, filt=False, deli='_',
                         rm_space=False)
    quantityPerPart = 0

    for sentence in getSentences(QQ):
        words = fenci(thu1, sentence)
        for word in words:
            if word[0] not in ['', ' ', '\n']:
                wordQuantity += 1
                if word[0] in dict:
                    dict[word[0]] += 1
                else:
                    dict[word[0]] = 1

    for i in dict:
        wordList.append([i, dict[i]])

    wordList.sort(key=lambda x: x[1], reverse=True)
    # 频率表-百分比
    for i in wordList:
        frequencyList.append([i[0], round(i[1] / wordQuantity, 5)])
    # 柱状图-每部分的数量
    quantityPerPart = wordList[0][1] // seg + 1

    histograms_x = np.linspace(1, quantityPerPart * seg, seg)
    histograms_y = np.arange(seg)
    histograms_y.fill(0)

    for i in wordList:
        histograms_y[i[1] // quantityPerPart] += 1

    plt.bar(histograms_x, histograms_y, width=20)
    print(quantityPerPart)
    print(histograms_y)
    print("出现次数：" + str(wordList))
    print("词典长度：" + str(len(wordList)))
    print("词频：" + str(frequencyList))
    print("单词总数:" + str(wordQuantity))

    with open("D:\programming\wordResult\wordFrequency" + "_" + QQ + ".txt", "w") as f:
        f.write(str(wordList))
        f.write("\n")
        f.write(str(frequencyList) + '\n')
        f.write("lenth:" + str(len(wordList)) + '\n')
        f.write("quantity:" + str(wordQuantity))
    plt.show()

    words = []
    for i in range(seg):
        words.append(wordList[i][0])
        histograms_y[i] = wordList[i][1]

    # plt.bar(words,histograms_y,width = 0.8)
    # plt.show()


def findMostFrequencyCharacter(QQ=None):  # 若为空则选择全部
    dict = {}
    ltrList = []
    frequencyList = []
    letterQuantity = 0
    histograms_x = np.array([])
    histograms_y = np.array([])
    seg = 30
    quantityPerPart = 0
    # 字数统计 单字出现次数统计
    for sentence in getSentences(QQ):
        for letter in sentence:
            if letter not in ['', ' ', '\n']:
                letterQuantity += 1
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1

    # 出现次数排序
    for i in dict:
        ltrList.append([i, dict[i]])
    ltrList.sort(key=lambda x: x[1], reverse=True)
    llDF = pd.DataFrame.from_records(ltrList)

    # 频率计算
    for i in ltrList:
        frequencyList.append([i[0], round(i[1] / letterQuantity, 5)])
    flDF = pd.DataFrame.from_records(frequencyList)
    display.display(
        flDF.describe(percentiles=[0.1, 0.2, 0.3, .4, .5, .6, .65, .7, .75, .8, .85, .9, .95, .96, .97, .98, .99]))

    # 生成概率分布图
    y = [0]
    x = [0]
    z = []
    for i in range(50):
        y.append(frequencyList[i][1] + y[i])
        x.append(i)
        z.append(frequencyList[i][0])
    saveList(z)

    npy = np.array(y)
    npx = np.array(x)
    fig, ax = plt.subplots()
    ax.plot(npx, npy)
    ax.set(xlabel='x', ylabel='percent',
           title='')
    ax.grid()
    fig.savefig("test.png")
    plt.show()
    # 出现次数分布图
    quantityPerPart = ltrList[0][1] // seg + 1
    histograms_x = np.linspace(1, quantityPerPart * seg, seg)
    histograms_y = np.arange(seg)
    histograms_y.fill(0)
    for i in ltrList:
        histograms_y[i[1] // quantityPerPart] += 1
    plt.bar(histograms_x, histograms_y, width=20)

    print(quantityPerPart)
    print(histograms_y)

    display.display(llDF.describe())
    print("单字出现次数：" + str(ltrList))
    print("字典长度：" + str(len(ltrList)))
    print("字频：" + str(frequencyList))
    print("字数：" + str(letterQuantity))

    with open("D:\programming\wordResult\letterFrequency" + "_" + str(QQ) + ".txt", "w") as f:
        f.write(str(ltrList))
        f.write("\n")
        f.write(str(frequencyList) + '\n')
        f.write("lenth:" + str(len(ltrList)) + '\n')
        f.write("quantity:" + str(letterQuantity))
    plt.show()

    words = []
    for i in range(seg):
        words.append(ltrList[i][0])
        histograms_y[i] = ltrList[i][1]

    # plt.bar(words,histograms_y,width = 0.8)
    # plt.show()


if __name__ == '__main__':
    findMostFrequencyCharacter()
