'''
对应的颜色简写：
b	蓝色	m	magenta(品红）
g	绿色	y	黄色
r	红色	k	黑色（black）
c	青色（cyan）	w	白色
使用十六进制表示颜色，如#0F0F0F
使用浮点数的字符串表示，即灰度表示方法，如color=“0.4”
使用浮点数的RGB元组表示，如（0.1, 0.3, 0.5）
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,0.1)
y=x*2
plt.plot(x,y,color="c")
plt.plot(x,y+1,color="#0F0F0F")
plt.plot(x,y+2,color="0.5")
plt.plot(x,y+3,color=(0.1,0.3,0.5))
plt.show()
'''
线的样式：
用linestyle表示，共有4种，
实线	-
虚线	--
点画线	-.
点线	：
前一篇博客已经讲过，表示颜色样式可以使用样式字符串来简单表示样式：
fmt = “[color][marker][linestyle]”
如“cx--”就表示青色线段，点的标记是x，用虚线表示。
'''
'''
子图，多图
多图（即同时生成多张图）只需要同时新建多个figure对象即可

子图subplot：(下面的例子是采用面向对象的方法用建立的figure对象添
加子图即add_subplot，也可以直接使用plt.subplot形成子图。

'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,0.1)
print(x)
#建立一个figure对象
fig=plt.figure()
#新建子图实例并绘图
ax1=fig.add_subplot(221)
ax1.plot(x,x*2,"r")
#新建子图2实例并绘图
ax2=fig.add_subplot(222)
ax2.plot(x,-x,"b")
#新建子图3实例并绘图
ax3=fig.add_subplot(223)
ax3.plot(x,-2*x,"k")
#新建子图4实例并绘图
ax4=fig.add_subplot(224)
ax4.plot(x,x**2,"y")
plt.show()
'''
网格grid
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,1)
plt.grid(color="r",linewidth="3")
plt.plot(x,x**2)
plt.show()
'''
图例legend: 下面是两种方法生成图例的代码，注意legend的参数，loc表示位置，
如果有多组曲线，ncol可以将其设置为多列，默认为1列。还有阴影shadow等参数，
'''
#使用plt.legend
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,1)
plt.plot(x,x**2)
#legend的参数loc可以指定图例的位置，此处0代表最合适的位置
plt.legend(loc=0)
plt.show()
#使用面向对象的方法
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,1)
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(x,x*2)
ax.legend(["line"])
plt.show()