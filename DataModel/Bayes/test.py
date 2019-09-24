from DataModel.Bayes import textClassify
listOPosts,listClasses=textClassify.loadDataSet()
print(listOPosts)
myVocabList=textClassify.createVocabList(listOPosts)
print(myVocabList)
print(textClassify.setOfWords2Vec(myVocabList,listOPosts[0]))
trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(textClassify.setOfWords2Vec(myVocabList,postinDoc))
p0V,p1V,pAb=textClassify.trainNB0(trainMat,listClasses)
print("第一个类别的概率")
print(p0V,pAb)
print("第二个类别的概率")
print(p1V,pAb)