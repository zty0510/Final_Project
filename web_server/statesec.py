# =============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
# =============================================================================#
import csv
import os
from typing import Tuple
from data_source.fr24_crawler import Fr24Crawler
import controller as cr
import time
import matplotlib.pyplot as plt

def get_modified_time(file):
    if os.path.exists(file):
        return time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getmtime(file)))
    else:
        return FileNotFoundError

def get_created_time(file):
    if os.path.exists(file):
        return time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getctime(file)))
    else:
        return FileNotFoundError

class State():


    def __init__(self):
        self.past_Airline_Quantity = 0  # 过去飞机数量
        self.now_Airline_Quantity = 0  # 现在飞机数量


    def init(self):
        csvfile = open("online_data.csv", encoding="utf-8")
        content = csv.reader(csvfile)
        rows = [row for row in content]
        data = rows[1]
        center_Lon = data[0]
        center_Lat = data[1]
        northeastern_Lon = data[2]
        northeastern_Lat = data[3]
        self.blink_interval = data[4]
        self.crawler_interval = data[5]

        self.data = Fr24Crawler([float(center_Lon), float(center_Lat)],
                                [float(northeastern_Lon), float(northeastern_Lat)])
        # self.num = self.data.get_Quantity_Binary_List()
        # self.change = self.data.get_change_bool()
        self.control = cr.BaseController(red=6, yellow=13, green=19, blue=26)



    def light(self,blink_interval=5):
        self.control.split1()  # 间隔1 开始进行增减判断 同时标志后四位数据显示已经结束

        if self.change > 0:
            self.control.red_on()
        elif self.change == 0:
            self.control.yellow_on()
        else:
            self.control.green_on()

        time.sleep(blink_interval)
        self.control.split1()  # 间隔1 标志着增减判断结束
        '''
        前四位分割
        '''

        if self.num[0] == 1:
            self.control.red_on()
        if self.num[1] == 1:
            self.control.yellow_on()
        if self.num[2] == 1:
            self.control.green_on()
        if self.num[3] == 1:
            self.control.blue_on()
        time.sleep(blink_interval)
        self.control.split2()  # 间隔2 标志着前四位数据显示已经完成
        '''
        middle 4 digits
        '''
        if self.num[4] == 1:
            self.control.red_on()
        if self.num[5] == 1:
            self.control.yellow_on()
        if self.num[6] == 1:
            self.control.green_on()
        if self.num[7] == 1:
            self.control.blue_on()
        time.sleep(blink_interval)
        self.control.split2()  # 间隔2 标志着前四位数据显示已经完成

        '''

        后四位分割
        '''
        if self.num[8] == 1:
            self.control.red_on()
        if self.num[9] == 1:
            self.control.yellow_on()
        if self.num[10] == 1:
            self.control.green_on()
        if self.num[11] == 1:
            self.control.blue_on()
        time.sleep(blink_interval)
        self.control.off()



    def get_change_bool(self):##获取数量变换趋势
        past_Quantity = self.get_past_Airline_Quantity()
        now_Quantity = self.get_now_Airline_Quantity()
        if now_Quantity > past_Quantity:
            return 1                        #飞机数量增加，返回1
        if now_Quantity == past_Quantity:
            return 0                        #飞机数量不变，返回0
        if now_Quantity < past_Quantity:
            return -1                       #飞机数量减少，返回-1

    def set_now_Airline_Quantity(self, number):
        self.now_Airline_Quantity = number

    def get_now_Airline_Quantity(self):
        return self.now_Airline_Quantity

    def set_past_Airline_Quantity(self, number):
        self.past_Airline_Quantity = number

    def get_past_Airline_Quantity(self):
        return self.past_Airline_Quantity

    def update_Airline_Quantity(self, old, new):
        self.set_past_Airline_Quantity(old)
        self.set_now_Airline_Quantity(new)

    def spin(self):
        file = "web_server/online_data.csv"
        while True:
            if get_modified_time(file) == FileNotFoundError:
                print("未发现online_data.csv")
            else:
                old_time = get_modified_time(file)
                while old_time == get_modified_time(file):
                    self.init()
                    self.data.store_data()
                    self.draw_pic()
                    self.set_past_Airline_Quantity(self.get_now_Airline_Quantity())
                    self.set_now_Airline_Quantity(self.data.get_now_Airline_Quantity())
                    self.num = self.data.get_Quantity_Binary_List()
                    self.change = self.get_change_bool()
                    print(self.num)
                    print(self.change)
                    self.light(float(self.blink_interval))
                    time.sleep(float(self.crawler_interval))
                    self.control.release()
                print('发现新文件')
                self.control.release()



    def draw_pic(self):
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
        x_axis = ('0-100', '100-200', '200-300', '300-400', 'NONE')
        y_axis = [num1, num2, num3, num4, nonumber]
        plt.bar(x_axis, y_axis)
        plt.title("altitude")
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
        plt.title("groundspeed")
        plt.savefig('static/image/groundspeed.png')
        plt.clf()
