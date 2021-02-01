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
            res[da[1]]['z'].append(da[4])
            res[da[1]]['w'].append(da[5])
        else:
            res[da[1]] = {}
            res[da[1]]['x'] = [da[3]]
            res[da[1]]['y'] = [da[2]]
            res[da[1]]['z'] = [da[4]]
            res[da[1]]['w'] = [da[5]]
    return res


def changeData(x, y, z, w):
    rx = [];
    ry = [];
    timeuse = 0
    print(len(x))
    flag = 1
    for i in range(len(x)):
        a=z[i]
        b=w[i]
        if z[i]  and w[i] :
            if z[i + 1]  and w[i + 1] :
                if (i == len(x) - 1):
                    break;
                tempx = (x[i + 1] == x[i])
                if tempx:
                    tempy = (y[i + 1] - y[i]).seconds
                    if tempy <= 300:
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
            else:
                if flag == 0:
                    rx.append(x[i - 1])
                    ry.append(timeuse / 60)
                    timeuse = 0
        else:
            if flag == 0:
                rx.append(x[i - 1])
                ry.append(timeuse / 60)
                timeuse = 0

    return rx, ry


def plotGraph(data):
    #    fig=plt.figure()
    #    ax=fig.add_subplot(1,1,1)
    #    ax.set_xlabel="星期排列"
    #    ax.set_ylabel="用水时长"
    df = pd.DataFrame(columns=('mac', 'date', 'time'))

    plt.title('中间停水间隔小于5分钟算作一次用水')  # 显示图表标题
    plt.xlabel('用水日期（单位：天）')  # x轴名称
    plt.ylabel('用水时长(单位：分钟)')  # y轴名称
    plt.grid(True)
    for key in data:
        print(key)
        kx, ky = changeData(data[key]['x'], data[key]['y'], data[key]['z'], data[key]['w'])
        #        ax.scatter(kx,ky)
        df1 = pd.DataFrame({'mac': key, 'date': kx,
                            'time': ky})
        df = pd.concat([df, df1])
        plt.scatter(kx, ky)
    print(df)
    # df.to_excel("D:\\工作资料\\大数据工作资料\\燃热零冷水\\dealresult.xlsx")
    plt.show()


def main():
    data = readData("D:\\工作资料\\大数据工作资料\\燃热零冷水\\input.xlsx");
    drawdata = dealData(data)
    plotGraph(drawdata)


if __name__ == '__main__':
    main()