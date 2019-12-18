#1、导入到pandas库中
import pandas as pd
#2、生成重复数据
data1,data2,data3,data4=['a',3],['b',2],['a',3],['c',2]
df=pd.DataFrame([data1,data2,data3,data4],columns=['col1','col2'])
print(df)
#3、判断重复数据
isDuplicated=df.duplicated()
print(isDuplicated)#打印输出
#4、剔除重复值
print(df.drop_duplicates())
print(df.drop_duplicates(['col1']))
print(df.drop_duplicates(['col2']))
print(df.drop_duplicates(['col1','col2']))