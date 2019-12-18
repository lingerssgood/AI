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
#迭代DataFrame
N=20
df=pd.DataFrame({
   'A':pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x':np.linspace(0,stop=N-1,num=N),
   'y':np.random.rand(N),
   'C':np.random.choice(['Low','Medium','High'],N).tolist(),
   'D':np.random.normal(100,10,size=(N)).tolist()
})
for col in df:
   print(col)
'''
iteritems() - 迭代(key，value)对
iterrows() - 将行迭代为(索引，系列)对
itertuples() - 以namedtuples的形式迭代行
'''
#iteritems()
#将每个列作为键，将值与值作为键和列值迭代为Series对象。
df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)
#iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列。
df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for row_index,row in df.iterrows():
   print(row_index,row)
#itertuples()方法将为DataFrame中的每一行返回一个产生一个
# 命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。
df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for row in df.itertuples():
   print(row)

#分割对象
# 应用一个函数
# 结合的结果
'''
聚合-计算汇总统计
转换-执行一些特定于组的操作
过滤-在某些情况下丢弃数据
'''
import pandas as pd
ipl_data={'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]
}
df=pd.DataFrame(ipl_data)
print(df)
#将数据拆成分组
#obj.groupby(‘key’)
# obj.groupby([‘key1’,’key2’])
# obj.groupby(key,axis=1)
#分组
print(df.groupby("Team"))
#查看分组
print(df.groupby("Team").groups)
print(df.groupby(['Team','Year']).groups)
#迭代遍历分组
#使用groupby对象，可以遍历类似itertools.obj对象
grouped=df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)
#选择一个分组
#使用get_group()，选择一个分组
print(grouped.get_group(2014))
#聚合
#聚合函数为每个组返回单个聚合值。当创建了分组(group by)对象，就可以对分组数据执行多个聚合操
# 作。一个比较常用的是通过聚合或等效的agg方法聚合
grouped=df.groupby('Year')#按年聚合
print(grouped['Points'].agg(np.mean))#求平均值
#查看分组大小的方法应用size()函数
grouped=df.groupby('Team')
print(grouped.agg(np.size))
#一次应用多个聚合函数
grouped=df.groupby('Team')
agg=grouped['Points'].agg([np.sum,np.mean,np.std])
print(agg)
#分组或列上的转换返回索引大小与被分组的索引相同的对象。
# 因此，转换应该返回与组块大小相同的结果。
grouped=df.groupby('Team')
score=lambda x:(x-x.mean())/x.std()*10
print(grouped.transform(score))
#过滤根据定义的标准过滤数据并返回数据的子集。
# filter()函数用于过滤数据。
filter=df.groupby('Team').filter((lambda x:len(x)>=3))
print(filter)




