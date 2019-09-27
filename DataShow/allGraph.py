import numpy as np
import matplotlib.pyplot as plt
#散点图
'''
1.numpy.random.rand() 
官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn) 
以给定的形状创建一个数组，并在数组中加入在[0,1]之间均匀分布的随机样本。
2.numpy.random.randn() 
官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn) 
以给定的形状创建一个数组，数组元素来符合标准正态分布N(0,1) 
若要获得一般正态分布则可用sigma * np.random.randn(…) + mu进行表示 
3.numpy.random.randint() 
官方文档中给出的用法是：numpy.random.randint(low,high=None,size=None,dtype) 
生成在半开半闭区间[low,high)上离散均匀分布的整数值;若high=None，则取值区间变为[0,low) 
4.numpy.random.random_integers() 
官方文档中给出的用法是： 
numpy.random.random_integers(low,high=None,size=None) 
生成闭区间[low,high]上离散均匀分布的整数值;若high=None，则取值区间变为[1,low] 
此外，若要将【a,b】区间分成N等分，也可以用此函数实现 
a+(b-a)*(numpy.random.random_integers(N)-1)/(N-1)
5.numpy.random_sanmple() 
官方文档中给出的用法是： 
numpy.random.random_sample(size=None) 
以给定形状返回[0,1)之间的随机浮点数 
其他函数，numpy.random.random() ;numpy.random.ranf() 
numpy.random.sample()用法及实现都与它相同

6.numpy.random.choice() 
官方文档中给出的用法： 
numpy.random.choice(a,size=None,replace=True,p=None) 
若a为数组，则从a中选取元素；若a为单个int类型数，则选取range(a)中的数 
replace是bool类型，为True，则选取的元素会出现重复；反之不会出现重复 
p为数组，里面存放选到每个数的可能性，即概率 
'''
N=1000
x=np.random.randn(N)
y=np.random.randn(N)
plt.scatter(x,y)
plt.show()
'''折线图
在-10到10之间生成100个数的等差数列，即在10到10之间
等间隔取100个数
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y, "ro--")
plt.show()
'''
3、条形图bar
'''
import numpy as np
import matplotlib.pyplot as plt
N=5
y=[4,6,2,1,6]
index=np.arange(N)
plt.bar(index,y)
plt.show()
'''
并列条形图
'''
import numpy as np
import matplotlib.pyplot as plt
index=np.arange(4)
a=[32,54,67,90]
b=[44,33,67,98]
bar_width=0.3
plt.bar(index,a,bar_width,color="b")
plt.bar(index+bar_width,b,bar_width,color="r")
plt.show()
'''
绘制直方图:hist
hist的参数：x是矩阵或矩阵序列。bins是整数或序列，如果是序列的话，横轴可以是不等间隔的。normed是是否标准化的意思，若为False,则纵轴显示数据的个数，
不过现在这个参数已经被弃用，而是用desity来代替。
arr: 需要计算直方图的一维数组
bins: 直方图的柱数，可选项，默认为10
normed: 是否将得到的直方图向量归一化。默认为0
facecolor: 直方图颜色
edgecolor: 直方图边框颜色
alpha: 透明度
'''
import numpy as np
import matplotlib.pyplot as plt
mu=100
sigma=20
x=mu+sigma*np.random.randn(2000)
plt.hist(x,bins=10,color="r",edgecolor="black",density="True")
plt.show()
'''
2-D直方图
bins=横竖分为几条
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(1000)+2
y=np.random.randn(1000)+5
plt.hist2d(x,y,bins=50)
plt.show()
'''
饼图pie
pie的参数x表示数据列表。 
labels表示类别标签列表，是一系列字符串。
 autopct可以显示各部分的占比。 explode突出显示某些部分。
'''
import numpy as np
import matplotlib.pyplot as plt
labels="A","B","C","D"
fracs=[15,29,89,54]
explode=[0,0.1,0,0]#设置突出显示的部分
plt.axes(aspect=1)#是坐标轴横纵等距
#autopct在饼状图内部显示出相应的数据（百分比）
plt.pie(x=fracs,labels=labels,autopct="%.0f%%",explode=explode)
plt.show()
'''
箱形图（箱线图）：boxplot实现。
显示一组数据的统计分散情况
（上边缘、上四分位数、中位数、下四分位数、下边缘、异常值）
'''
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)
data=np.random.normal(size=1000,loc=0,scale=1)
#sym改变异常值的显示形状，whis表示虚线的长度
plt.boxplot(data,sym="o",whis=1.5)
plt.show()
'''
同时绘制多个图
'''
import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(size=(1000,4),loc=0,scale=1)
labels=["A","B","C","D"]
plt.boxplot(data,labels=labels)
plt.show()