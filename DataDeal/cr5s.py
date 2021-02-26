"""
Created on Tue Jul 23 10:40:58 2019

@author: 01517007
"""

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1、导入数据
# 2、处理数据：比较连续两条数据的时间间隔是否小于等于5分钟，小于5分钟保留并做累加；记录X为week,纵轴为累计的时间单位为分钟
from matplotlib.ticker import MultipleLocator

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def readData(fileName):
    data = pd.read_excel(fileName)
    return np.array(data)


def dealData(data):
    res = {}
    for da in data:
        if da[1] in res:
            res[da[1]]['x'].append(da[3])
            res[da[1]]['y'].append(da[2])
        else:
            res[da[1]] = {}
            res[da[1]]['x'] = [da[3]]
            res[da[1]]['y'] = [da[2]]
    return res


def changeData(x, y):
    rx = [];
    ry = [];
    timeuse = 0
    print(len(x))
    for i in range(len(x)):
        if (i == len(x) - 1):
            break;
        tempx = (x[i + 1] == x[i])
        if tempx:
            tempy = (y[i + 1] - y[i]).seconds
            if tempy <= 240:
                timeuse += tempy
                flag = 0
            else:
                rx.append(x[i])
                ry.append(timeuse / 60)
                timeuse = 0
                flag = 1
        else:
            if flag == 0:
                rx.append(x[i])
                ry.append(timeuse / 60)
                timeuse = 0
    return rx, ry


def plotGraph(data):
    #    fig=plt.figure()
    #    ax=fig.add_subplot(1,1,1)
    #    ax.set_xlabel="星期排列"
    #    ax.set_ylabel="用水时长"
    plt.title('中间停水间隔小于4分钟算作一次用水')  # 显示图表标题
    plt.xlabel('用水日期')  # x轴名称
    plt.ylabel('用水时长')  # y轴名称
    plt.grid(True)
    for key in data:
        print(key)
        kx, ky = changeData(data[key]['x'], data[key]['y'])
        #        ax.scatter(kx,ky)
        plt.scatter(kx, ky,  marker='>')

    # x_major_locator = MultipleLocator(1)
    # # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(5)
    # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # # ax为两条坐标轴的实例
    # ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为5的倍数
    # plt.xlim(-0.5, 11)
    # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(0, 50)
    # 把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白

    plt.show()


def main():
    data = readData("D:\\工作资料\\大数据工作资料\\燃热零冷水\\data-cr5s.xlsx");
    drawdata = dealData(data)
    plotGraph(drawdata)


if __name__ == '__main__':
    main()