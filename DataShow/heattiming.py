import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlwt
import pymysql


def readData(fileName):
    data = pd.read_excel(fileName)
    return np.array(data.values)


def getSqlConn(host, user, password, db):
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()
    return conn, cursor


def getDataUnionSQL(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return np.array(data)


def dealData(data):
    res = {}
    for da in data:
        if da[3] in res:
            res[da[3]]['x'].append(da[1])
            res[da[3]]['y'].append(da[2])
            res[da[3]]['z'].append(da[3])

        else:
            res[da[3]] = {}
            res[da[3]]['x'] = [da[1]]
            res[da[3]]['y'] = [da[2]]
            res[da[3]]['z'] = [da[3]]
    return res


def changeData(x, y, z):
    rx = [];
    ry = [];
    for i in range(len(x)):
        if i == len(x) - 1:
            break
        if x[i] == 2 and x[i + 1] == 2:
            tempy = (y[i + 1] - y[i]).seconds
            print(tempy)
            ry.append(tempy)
            rx.append(z[i])
    return rx, ry


def outputdata(data):
    df = pd.DataFrame(columns=('mac', 'time'))

    for key in data:
        print(key)
        kx, ky = changeData(data[key]['x'], data[key]['y'], data[key]['z'])
        df1 = pd.DataFrame({'mac': kx, 'time': ky})
        df = pd.concat([df, df1])
    df.to_excel("C:\\Users\\01517007\\Desktop\\平均加热时长_deal.xls")
    plt.show()


def main():
    # data = readData("C:\\Users\\01517007\\Desktop\\平均加热时长1.xls");
    conn, cursor = getSqlConn('10.163.202.223:3306', 'water_admin_dev', 'water_admin_dev','bigdata')
    data = getDataUnionSQL(cursor,
                           'select currentWaterFlux, heatingStatus, from_unixtime(event_time_stamp/1000),mac_id from source_data group by mac_id,event_time_stamp order by mac_id,event_time_stamp limit 10000')
    drawdata = dealData(data)
    outputdata(drawdata)


if __name__ == '__main__':
    main()
