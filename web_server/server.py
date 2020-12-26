# =============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
# =============================================================================#
from flask import Flask, request, render_template
import fr24_crawler
import csv

import os
import matplotlib.pyplot as plt
import time
import threading
import multiprocessing
web_server = Flask(__name__)
web_server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def crawler():
    while True:
        csvfile = open("online_data.csv", encoding="utf-8")
        content = csv.reader(csvfile)
        rows = [row for row in content]
        data = rows[1]
        center_Lon = data[0]
        center_Lat = data[1]
        northeastern_Lon = data[2]
        northeastern_Lat = data[3]
        LED_time = data[4]
        crawler_interval = data[5]
        crawler = fr24_crawler.Fr24Crawler([float(center_Lon), float(center_Lat)],
                                           [float(northeastern_Lon), float(northeastern_Lat)])
        crawler.store_data()
        print(crawler.get_Quantity_Binary_List())
        print(crawler.get_change_bool())
        # 生成图像‘altitude.png’
        csvfile = open("csv_data.csv", encoding="utf-8")
        content = csv.reader(csvfile)
        rows = [row for row in content]
        key = rows[0]
        del rows[0]
        list = []
        for values in rows:
            dic = dict(map(lambda x, y: [x, y], key, values))
            list.append(dic)
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        nonumber = 0
        for data in list:
            if data['altitude'] == '':
                data['altitude'] = 1000
        for data in list:
            if int(data['altitude']) <= 100:
                num1 += 1
            elif 100 < int(data['altitude']) <= 200:
                num2 += 1
            elif 200 < int(data['altitude']) <= 300:
                num3 += 1
            elif 300 < int(data['altitude']) <= 400:
                num4 += 1
            else:
                nonumber += 1
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        x_axis = ('0-100', '100-200', '200-300', '300-400', '未得到数据')
        y_axis = [num1, num2, num3, num4, nonumber]
        plt.bar(x_axis, y_axis)
        plt.savefig('static/image/altitude.png')
        plt.clf()
        # 生成‘groundspeed的图像’
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        nonumber = 0
        for data in list:
            if data['groundspeed'] == '':
                data['groundspeed'] = 1000
        for data in list:
            if int(data['groundspeed']) <= 175:
                num1 += 1
            elif 175 < int(data['groundspeed']) <= 350:
                num2 += 1
            elif 350 < int(data['groundspeed']) <= 525:
                num3 += 1
            elif 525 < int(data['groundspeed']) <= 700:
                num4 += 1
            else:
                nonumber += 1
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        x_axis = ('0-175', '175-350', '350-525', '525-700', '未得到数据')
        y_axis = [num1, num2, num3, num4, nonumber]
        plt.bar(x_axis, y_axis)
        plt.savefig('static/image/groundspeed.png')
        plt.clf()

        time.sleep(int(crawler_interval))


@web_server.route('/')
def home():
    return render_template('home.html')


@web_server.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        center_Lon = request.form.get('center_Lon')  # 从form处获取POST信息
        center_Lat = request.form.get('center_Lat')
        northeastern_Lon = request.form.get('northeastern_Lon')
        northeastern_Lat = request.form.get('northeastern_Lat')
        LED_time = request.form.get('LED_time')
        crawler_interval = request.form.get('crawler_interval')
        path = os.path.abspath(".") + r"/online_data.csv"  # 获取当前目录绝对路径
        with open(path, "w+") as f:
            f.write("center_Lon,center_Lat,northeastern_Lon,northeastern_Lat,crawler_interval,LED_time")
            f.write("\n")
        with open(path, "a+", newline="") as f:
            writec = csv.writer(f)
            row = [center_Lon, center_Lat, northeastern_Lon, northeastern_Lat, LED_time, crawler_interval]
            writec.writerow(row)

@web_server.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        center_Lon = request.form.get('center_Lon')  # 从form处获取POST信息
        center_Lat = request.form.get('center_Lat')
        northeastern_Lon = request.form.get('northeastern_Lon')
        northeastern_Lat = request.form.get('northeastern_Lat')
        LED_time = request.form.get('LED_time')
        crawler_interval = request.form.get('crawler_interval')
        path = os.path.abspath(".") + r"/online_data.csv"  # 获取当前目录绝对路径
        with open(path, "w+") as f:
            f.write("center_Lon,center_Lat,northeastern_Lon,northeastern_Lat,crawler_interval,LED_time")
            f.write("\n")
        with open(path, "a+", newline="") as f:
            writec = csv.writer(f)
            row = [center_Lon, center_Lat, northeastern_Lon, northeastern_Lat, LED_time, crawler_interval]
            writec.writerow(row)

    csvfile = open("online_data.csv", encoding="utf-8")
    content = csv.reader(csvfile)
    rows = [row for row in content]
    data = rows[1]
    center_Lon = data[0]
    center_Lat = data[1]
    northeastern_Lon = data[2]
    northeastern_Lat = data[3]
    blink_interval = data[4]
    crawler_interval = data[5]
    dic = {
        'loc': [center_Lon, center_Lat],
        'rng': [northeastern_Lon, northeastern_Lat],
        'LED_time': (blink_interval),
        'crawler_time': (crawler_interval),
    }

    return render_template('config.html', **dic)


@web_server.route('/showdata')
def showdata():
    csvfile = open("csv_data.csv", encoding="utf-8")
    content = csv.reader(csvfile)
    rows = [row for row in content]
    key = rows[0]
    del rows[0]
    list = []
    for values in rows:
        dic = dict(map(lambda x, y: [x, y], key, values))
        list.append(dic)
    return render_template('showdata.html', data=list)


@web_server.route('/vis', methods=['GET'])
def vis():
    return render_template('vis.html')


# def picture_altitude():


if __name__ == "__main__":
    web_server.run(debug=False, host="127.0.0.1", port=5000)
