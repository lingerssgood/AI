#1、 导入数据
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
# 2、生成缺失数据
df=pd.DataFrame(np.random.randn(6,4),columns=['col1','col2','col3','col4'])
df.iloc[1:2,1]=np.nan
df.iloc[4,3]=np.nan
print(df)
#3、 判断缺失值
nan_all=df.isnull()#获取所有的空值
print(nan_all)
nan_col1=df.isnull().any()#含nan的列,至少1个
nan_col2=df.isnull().all()#全部为nan的列
print(nan_col1)
print(nan_col2)
#4、丢弃缺失值
df2=df.dropna()#丢弃含有nan的记录
print(df2)
#5、通过sklearn的数据预处理方法对缺失值进行处理,以均值替换
#strategy可以是median或者most_frequent
#axis=0,用列做计算逻辑
nan_model=Imputer(missing_values='NaN',strategy='mean',axis=0)
nan_result=nan_model.fit_transform(df)#应用模型
print(nan_result)
#6、用pandas做缺失值处理
nan_result_pd1=df.fillna(method='backfill')#用后面的值替换缺失值
nan_result_pd2=df.fillna(method='bfill',limit=1)#用后面的值替代缺失值，限制每列只能替代一个缺失值
nan_result_pd3=df.fillna(method='pad')#用前面的值替代缺失值或者参数ffill
nan_result_pd4=df.fillna(0)#用0替代缺失值
nan_result_pd5=df.fillna({'col1':1.1,'col4':1.2})#用不同值替换不同列的缺失值
nan_result_pd6=df.fillna(df.mean()['col1':'col4'])#用各自列的平均值替换缺失值
print(nan_result_pd1)
print(nan_result_pd2)
print(nan_result_pd3)
print(nan_result_pd4)
print(nan_result_pd5)
print(nan_result_pd6)
nan_result_pd7=df.replace(np.nan,0)





