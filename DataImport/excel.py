#1：读取数据
#2：对行列进行操作
#3：处理行列数据成为字典
import pandas as pd
#默认读取第一个表单
def readDaultSheet(address):
    df=pd.read_excel(address)
    data=df.head()
    print("获取到所有的值:\n{0}".format(data))#格式化输出
    return df
# def readAssign
