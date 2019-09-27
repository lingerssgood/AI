import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5*np.pi,100)
y1=np.sin(x)
y2=np.sin(2*x)
'''
填充两条线曲线与x轴之间的区域

'''
plt.fill(x,y1,color="red",alpha=0.3)
plt.fill(x,y2,color="blue",alpha=0.3)
plt.show()
'''
填充图形之间的区域，采用fill_between
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5*np.pi,100)
y1=np.sin(x)
y2=np.sin(2*x)
#绘制两条正弦曲线
plt.plot(x,y1,"b")
plt.plot(x,y2,"b")
'''
填充两条曲线之间的部分，where是条件
表达式（在满足条件的区域内填充即可）
interpolate是精细化填充的参数，
防止取样点较少造成有些区域没有填充
'''
plt.fill_between(x,y1,y2,where=y1>y2,facecolor="red",alpha=0.4,interpolate=True)
plt.fill_between(x,y1,y2,where=y1<=y2,facecolor="yellow",alpha=0.4,interpolate=True)
plt.show()
'''
在图形上画一些常见的形状，如：三角形、圆、多边形等等
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig,ax=plt.subplots()
xy1=np.array([0.2,0.2])
print(xy1)
xy2=np.array([0.2,0.8])
xy3=np.array([0.8,0.2])
xy4=np.array([0.8,0.8])
#生产circle对象并添加到窗口
circle=mpatches.Circle(xy1,0.1)
ax.add_patch(circle)
#生产矩阵对象并添加到窗口
rect=mpatches.Rectangle(xy2,0.2,0.1,color="r")
ax.add_patch(rect)
#生产多边形对象并添加到窗口
polygon=mpatches.RegularPolygon(xy3,5,0.1,color="g")
ax.add_patch(polygon)
#生成椭圆对象并添加到窗口
ellipse=mpatches.Ellipse(xy4,0.4,0.2,color="y")
ax.add_patch(ellipse)
plt.axis("equal")#横纵坐标轴等距
plt.grid()
plt.show()
'''
极坐标的简单绘制
'''
import numpy as np
import matplotlib.pyplot as plt
#生成极坐标的极经
r=np.arange(1,6,1)
#生成极坐标的极角
theta=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]
ax=plt.subplot(111,projection="polar")
ax.plot(theta,r,color="r",linewidth=3)
ax.grid(True)
plt.show()