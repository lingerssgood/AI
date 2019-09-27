import numpy as np
from matplotlib import pyplot as plt
import matplotlib
zhfont=matplotlib.font_manager.FontProperties(fname="OpenSans-Bold.ttf")
x=np.arange(1,11)
print('打印出：',x)
y=2*x+5
plt.title("第一个matplotlib",fontproperties=zhfont)#绘制标题
plt.xlabel("横坐标轴标签",fontproperties=zhfont)#绘制X轴
plt.ylabel("纵坐标轴标签",fontproperties=zhfont)#绘制Y轴
plt.plot(x,y,"ob")#绘制X,Y轴
plt.show()#展示图形

import numpy as np
import matplotlib.pyplot as plt
# 计算正弦曲线上点的 x 和 y 坐标
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.title("sine wave form")
plt.plot(x,y,"ob")
plt.show()
#subplot()用法---一个图形上不同的东西
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
print(x)
y_sin=np.sin(x)
y_cos=np.cos(x)
#激活第一个subplot
plt.subplot(2,1,1)
#绘制第一个图像
plt.plot(x,y_sin)
plt.title('sine')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine')
plt.show()
#bar用法
from matplotlib import pyplot as plt
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.bar(x,y,align='center')
plt.bar(x2,y2,color='g',align='center')
plt.title('Bar graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
#numpy.histogram
import numpy as np
a=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a,bins=[0,20,40,60,80,100])
hist,bins=np.histogram(a,bins=[0,20,40,60,80,100])
print(hist)
print(bins)
#转换成直方图形状
from matplotlib import pyplot as plt
import numpy as np
a=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title("histogram")
plt.show()
#matplotlib下面汉字的用法
from matplotlib import pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
year=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
y_data=[100,200,300,400,500,600,700]
plt.plot(year,gdp,"go-",year,y_data,"rp-.")
plt.title("名义GDP")
plt.ylabel("十亿美元")
plt.show()