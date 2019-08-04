#数据处理过程
#1:收集数据：可以使用任何方法
#2：准备数据：距离计算所需要的数值，最好是结构化的数据格式
#3：分析数据：可以使用任何方法
#4：训练算法此步骤不适用K近邻算法
#5：测试算法：计算错误率
#6：使用算法：首先需要输入样本数据和结构化的输出结果，然后运行K-近邻算法判定输入数据分别属于哪个分类，最后应用对计算出的分类执行后续的处理
from numpy import *
import operator
#解析数据，加载已知数据所属类别
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
#从文本文件中解析数据
#功能：使用K近邻算法将每组数据划分到某个类中
#对未知类别属性的数据集中的每个点依次执行以下操作：
#1：计算已知类别数据集中的点与当前点之间的距离
#2：按照距离递增次序排序
#3：选取与当前点距离最小的K个点
#4：确定前K个点所在类别出现概率
#5：返回前K个点出现概率最高的类别作为当前点的预测分类
def classfy0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
