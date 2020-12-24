# =============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
# =============================================================================#
from typing import Tuple
from data_source.fr24_crawler import Fr24Crawler
import controller as cr
import time


class State():
    def __init__(self, loc: Tuple[float, float], rng: float, red=6, yellow=13, green=19, blue=26):
        self.data = Fr24Crawler(loc, rng)
        self.num = self.data.get_Quantity_Binary_List()
        self.change = self.data.get_change_bool()
        self.control = cr.BaseController(red, yellow, green, blue)


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

    def spin(self,crawler_interval=1,blink_interval=5):
        n=0
        while True:
            if n==0:
                n+=1
            else:
                self.control.release()
            self.data.store_data()
            print(self.data.get_Quantity_Binary_List())
            print(self.data.get_change_bool())
            self.num = self.data.get_Quantity_Binary_List()
            self.change = self.data.get_change_bool()
            self.light(blink_interval)
            time.sleep(crawler_interval)

        raise NotImplementedError



