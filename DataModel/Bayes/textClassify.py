from numpy import *
'''
词表到向量的转换函数
'''
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec
def createVocabList(dataSet):
    vocabSet=set([])#创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document)#创建两个集合的并集
    return list(vocabSet)
def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)#创建所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word: %s is not in my Vocabbulary!"% word)
    return returnVec
'''
训练算法：从词向量计算概率
'''
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    print('第一个参数：',numTrainDocs)
    numWords=len(trainMatrix[0])
    print('第二个参数：',numWords)
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    # p0Num=zeros(numWords);p1Num=zeros(numWords)
    # p0Denom=0.0;p1Denom=0.0
    p0Num = ones(numWords);p1Num = ones(numWords)  # change to ones()
    p0Denom = 2.0;p1Denom = 2.0  # change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix)
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    # p1Vect=p1Num/p1Denom
    # p0Vect=p0Num/p1Denom
    p1Vect = log(p1Num / p1Denom)  # change to log()
    p0Vect = log(p0Num / p0Denom)  # change to log()
    return p0Vect,p1Vect,pAbusive
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))


