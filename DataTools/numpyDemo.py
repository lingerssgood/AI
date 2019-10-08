import numpy as np
'''
ndim:维度
shape:行数和列数
size:元素个数
'''
import numpy as np
array=np.array([[1,2,3],[2,3,4]])
print(array.ndim)
print(array.shape)
print(array.size)
'''
array：创建数组
dtype：指定数据类型
zeros：创建数据全为0
ones：创建数据全为1
empty：创建数据接近0
arrange：按指定范围创建数据
linspace：创建线段
'''
#创建数组
a=np.array([[2,23,4],[2,3,4]])
print(a)
#指定数据 dtype
a=np.array([23,24,56],dtype=np.int)
print(a)
a=np.array([23,24,56],dtype=np.float)
print(a)
a=np.array([23,24,56],dtype=np.int32)
print(a)
a=np.array([23,24,56],dtype=np.float32)
print(a)
#创建数据全为0
a=np.zeros((3,4))
print(a)
#创建一维数组
a=np.ones((3,4),dtype=np.int)
print(a)
a=np.empty((3,4))
print(a)
#用arange创建连续数组,10-19,间隔是2
a=np.arange(10,20,2)
print(a)
#reshape，改变数据的形状
a=np.arange(12).reshape((3,4))
print(a)
#创建线段数据,开始1，结束10，且分割成20个，生成线段
a=np.linspace(1,10,20)
print(a)
a=np.linspace(1,10,20).reshape(5,4)
print(a)
'''
基础运算
'''
import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])
#一维数据的计算
c=a+b
c=a*b
c=a-b
c=b**2
c=10*np.sin(a)#调用np中的数学函数
print(b<3)
'''
多行多维的运算
'''
#矩阵的乘法
a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))
c_dot=np.dot(a,b)
c_dot2=a.dot(b)
print(c_dot)
print(c_dot2)
import numpy as np
a=np.random.random((2,4))
#生成2行 4列的浮点数，浮点数都是从0-1中随机
print(a)
np.sum(a)
np.min(a)
np.max(a)
#axis=0，以列为主；axis=1,以行为主
print("a=",a)
print("sum=",np.sum(a,axis=1))
print("min=",np.sum(a,axis=0))
print("max=",np.sum(a,axis=1))