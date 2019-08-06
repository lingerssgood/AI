#K近邻算法改善约会网站的配对效果
from numpy import *
from pip._vendor.distlib.compat import raw_input
from  .import KNN_base
#准备数据
def file2Matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[-1]
        index+=1
    return returnMat,classLabelVector
#图形展示
import matplotlib
import matplotlib.pyplot as plt
def dataShow():
    datingDataMat,datingLabels=file2Matrix('datingtestset.txt')
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    plt.show()
    ax.scatter(datingDataMat[:,1],datingDataMat[:2],
               15.0*array(datingLabels),15.0*array(datingLabels))
#归一化特征值
def autoMorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals
#测试代码--错误率计算
def datingClassTest():
    hoRatio=0.10
    datingDataMat,datingLabels=file2Matrix('datingtestset.txt')
    normMat,ranges,minVals=autoMorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int[m*hoRatio]
    errorCount=0.0
    for i in range(numTestVecs):
        classifierResult=KNN_base.classfy0(normMat[i,:],normMat[numTestVecs:m,:],\
                                  datingLabels[numTestVecs:m],3)
        print("the classifier came back with:%d,the real answer is:%d"\
              %(classifierResult,datingLabels[i]))
        if(classifierResult!=datingLabels[i]):errorCount+=1.0
        print("the total error rate is %f"%(errorCount/float(numTestVecs)))
#构建完整系统
def classfyPerson():
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(raw_input(\
        "percentage of time spent playing video games?"))
    ffMiles=float(raw_input("frequent flier miles earned per year?"))
    iceCream=float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLables=file2Matrix('datingtestset.txt')
    normMat,ranges,minVals=autoMorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=KNN_base.classfy0((inArr-\
                                        minVals)/ranges,normMat,datingLables,3)
    print("You will probably like this person:",\
          resultList[classifierResult-1])