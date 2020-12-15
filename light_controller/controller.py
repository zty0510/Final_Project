# =============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
# =============================================================================#

import gpiozero
from time import sleep


class BaseController:

    def __init__(self, red, yellow, green, blue):
        self.red = gpiozero.LED(red)
        self.yellow = gpiozero.LED(yellow)
        self.green = gpiozero.LED(green)
        self.blue = gpiozero.LED(blue)

    def twinkling(self):
        self.red.off()
        freq = -1
        while int(freq) <= 0:
            freq = input("Please input frequency")
        if int(freq) > 0:
            self.red.blink(on_time=1 / (2 * int(freq)), off_time=1 / (2 * int(freq)))

    def split1(self):
        self.off()
        self.red.on()
        sleep(0.5)
        self.red.off()
        self.yellow.on()
        sleep(0.5)
        self.yellow.off()
        self.green.on()
        sleep(0.5)
        self.green.off()
        self.blue.on()
        sleep(0.5)
        self.blue.off()

    def split2(self):
        self.off()
        self.blue.on()
        sleep(0.25)
        self.blue.off()
        self.green.on()
        sleep(0.25)
        self.green.off()
        self.yellow.on()
        sleep(0.25)
        self.yellow.off()
        self.red.on()
        sleep(0.25)
        self.red.off()

    def red_on(self):
        self.red.on()


    def blue_on(self):
        self.blue.on()


    def green_on(self):
        self.green.on()


    def yellow_on(self):
        self.yellow.on()



    def off(self):
        self.red.off()
        self.blue.off()
        self.green.off()
        self.yellow.off()

