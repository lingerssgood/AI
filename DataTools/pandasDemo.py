#数组创建序列
import pandas as pd
import numpy as np
'''
pandas.Series( data, index, dtype, copy)。
可以使用各种输入创建一个系列，如 -
数组
字典
标量值或常数
'''
data=np.array(['a','b','c','d'])
s=pd.Series(data,index=[100,101,102,103])
print("数组创建系列：",s)
import pandas as pd
import numpy as np
data={'a':0,'b':1.,'c':2.}
s=pd.Series(data)
print("从字典创建的系列：",s)
'''
pandas.DataFrame( data, index, columns, dtype, copy)
Pandas数据帧(DataFrame)可以使用各种输入创建，如 - 
列表
字典
系列
Numpy ndarrays
另一个数据帧(DataFrame)
'''
import pandas as pd
#创建空的DataFrame
df=pd.DataFrame()
print(df)
#从列表创建DataFrame==单列值
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)
#多列值
data=[['Alex',10],['Bob',12],['Clarke',13]]
df=pd.DataFrame(data,columns=['Name','Age'])
print(df)
data=[['Alex',10],['Bob',12],['Clarke',13]]
df=pd.DataFrame(data,columns=['Name','Age'],dtype='float')
print(df)
#从ndarrays/Lists的字典来创建DataFrame
data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)
#使用数组创建一个索引的数据帧(DataFrame)。
data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)
#从列表创建数据帧DataFrame
#通过传递字典列表来创建数据帧(DataFrame)
import pandas as pd
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data)
print(df)
#通过传递字典列表和行索引来创建数据帧(DataFrame)
data=[{'a':1,'b':2},{'a':5,'b':'10','c':20}]
df=pd.DataFrame(data,index=['first','second'])
print(df)
#如何使用字典，行索引和列索引列表创建数据帧(DataFrame)
data=[{'a':1,'b':2},{'a':5,'b':'10','c':20}]
df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
print(df1)
df2=pd.DataFrame(data,index=['first','second'],columns=['a','b1'])
print(df2)
#从系列的字典来创建DataFrame
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print(df)
#列选择==column
print(df['one'])
#列添加
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
df['four']=df['one']+df['three']
print(df)
#列删除
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
   'three':pd.Series([10,20,30],index=['a','b','c'])}
df=pd.DataFrame(d)
print('our DatafFrame is:')
print(df)
print('Deleting the first column using DEL function:')
del df['one']
print(df)
print('Deleting another column using POP function:')
df.pop('two')
print(df)
#行的选择，添加及删除==index
#标签选择
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
   'three':pd.Series([10,20,30],index=['a','b','c'])}
df=pd.DataFrame(d)
print(df.loc['b'])
#整数位置选择
print(df.iloc[2])
#行切片
print(df[2:4])
print(df[1:2])
#附加行
df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
print(df)
print(df2)
df=df.append(df2)
print(df)
#删除行
df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=df.append(df2)
df=df.drop(0)
print(df)