#1：读取数据
#2：对行列进行操作
#3：处理行列数据成为字典
import pandas as pd
#默认读取第一个表单
def readDaultSheet(filePath):
    df=pd.read_excel(filePath)
    data=df.head()
    print("获取到所有的值:\n{0}".format(data))#格式化输出
    return df
#返回多表，默认sheet_name=0,a,b指定表单
def readMultiSheet(filePath,a,b):
    df=pd.read_excel(filePath,sheetname=[a,b])
    data=df.head()
    print("获取到所有的值:\n{0}".format(data))
    return df
#根据表头名称或者表的位置读取该表的数据
#说明：sheetname=表单名称;或者等于表单位置编号
def  readAssignSheet(filePath,sheetname):
    df=pd.read_excel(filePath,sheetname=sheetname)
    data=df.head()
    print("获取到所有的值:\n{0}".format(data))
    return df
#指定作为列名的行，默认0，即取第一行，数据为列名行以下的数据；若数据不含列名，则设定 header = None；
def readNoDatSheet(filePath,sheetname,header):
    df=pd.read_excel(filePath,sheetname=sheetname,header=header)
    data=df.head()
    print("获取到所有的值：\n{0}".format(data))
    return df
#从头开始略去指定行数的数据
def assignRowFromHeaderSheet(filePath,sheetname,header,skip_rows):
    df=pd.read_excel(filePath,sheetname=sheetname,header=header,skiprows=skip_rows)
    data=df.head()
    print("获取到所有的值：\n{0}".format(data))
    return df
#省略尾部的行数据
def assignRowFromFootSheet(filePath,sheetname,header,skip_footer):
    df=pd.read_excel(filePath,sheetname=sheetname,header=header,skip_footer=skip_footer)
    data=df.head()
    print("获取到所有的值：\n{0}".format(data))
    return df
#指定列为索引列
def assignColumnIndexSheet(filePath,sheetname,header,skip_footer,index_col):
    df= pd.read_excel(filePath, sheetname=sheetname, header=header, skip_footer=skip_footer, index_col=index_col)
    data=df.head()
    print("获取到所有的值：\n{0}".format(data))
    return df
#指定列的名字，传入一个list数据
def assignColnumNameSheet(filePath,sheetname,header,skip_footer,index_col,names):
    df= pd.read_excel(filePath, sheetname=sheetname, header=header, skip_footer=skip_footer, index_col=index_col,names=names)
    data=df.head()
    print("获取到所有的值：\n{0}".format(data))
    return df