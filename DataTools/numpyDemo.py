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
import numpy as np
a=np.arange(2,14).reshape(3,4)
print(a)
'''
random用法
'''
print(np.random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
print(np.random.random() )             # 产生 0 到 1 之间的随机浮点数
print(np.random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(np.random.choice(['Low','Medium','High'],20))   # 从序列中随机选取一个元素
print(np.random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
print(np.random.sample([1, '23', [4, 5]], 2))#random.sample([], n)，列表元素任意n个元素的组合，示例n=2
'''
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，
    scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
'''
mu, sigma = 0, .1
s = np.random.normal(loc=mu, scale=sigma, size=1000)


a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
np.random.shuffle(a)
print(a)
#argmin:最小元素索引；argmax:最大元素索引
print(np.argmin(a))
print(np.argmax(a))
#mean矩阵的均值
print(np.mean(a))
print(np.average(a))
print(a.mean())
#矩阵的中位数
# print(a.median())
#累加函数cumsum每累加一次，记一次值
print(np.cumsum(a))
#累差函数，计算每一行中后一项与前一项之差，3行4列得到3行3列矩阵
print(np.diff(a))
#返回数组a中非零元素的索引值数组。
#二维数组行返回，列也返回，零元素不返回
print(np.nonzero(a))
#排序
b=np.arange(14,2,-1).reshape((3,4))
print(b)
print(np.sort(b))
#矩阵转置
print(np.transpose(b))
print(b.T)
#clip(array,array_min,array_max)
#比最小值小的变成最小值，大的变成最大值
print(np.clip(b,5,9))
#一维索引
import numpy as np
c=np.arange(3,15)
print(c[3])
#一维转成二维
d=np.arange(3,15).reshape(3,4)
print(d)
print(d[2])#对应第三行
print(d[1][1])
print(d[1,1])
#切片
print(d[1,1:3])#从1开始不包括3
'''
逐行逐列打印
'''
for row in d:
    print(row)
for column in d.T:
    print(column)
    '''
  这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而flat是一个迭代器，本身是一个object属性。  
    '''
print(d.flatten())
for item in d.flat:
    print(item)
#Numpy array 合并
#按行、列多种方式合并
import numpy as np
a=np.array([1,1,1])
b=np.array([2,2,2])
print(np.vstack((a,b)))
'''
vertical stack本身属于一种上下合并，即对括号中的两个整体进行对应操作。
此时我们对组合而成的矩阵进行属性探究
'''
c=np.vstack((a,b))
print(a.shape,c.shape)
'''
利用shape函数可以让我们很容易地知道A和C的属性，从打印出的结果来看，A仅仅是一个拥有3项元素的数组（数列），
而合并后得到的C是一个2行3列的矩阵。
介绍完了上下合并，我们来说说左右合并：
'''
d=np.hstack((a,b))
print(d)
print(a.shape,d.shape)
'''
说完了array的合并，我们稍稍提及一下前一节中转置操作，如果面对如同前文所述的A序列， 转置操作便很有可能无法对其进行转置（因为A并不是矩阵的属性），
此时就需要我们借助其他的函数操作进行转置：
'''
print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)
print(a[:,np.newaxis])
print(a[:,np.newaxis].shape)
'''
结合着上面的知识，我们把它综合起来：
'''
import numpy as np

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack

print(D)
print(A.shape, D.shape)
'''
当你的合并操作需要针对多个矩阵或序列时，
借助concatenate函数可能会让你使用起来比前述的函数更加方便：
'''
c=np.concatenate((a,b,b,a),axis=0)#按行
print(c)
d=np.concatenate((a,b,b,a),axis=1)#按列
print(d)