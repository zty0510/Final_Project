#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from gpiozero import LED
from time import sleep


class BaseController:

    def __init__(self):
        raise NotImplementedError

    def work_once(self):
        raise NotImplementedError

    def on(self):
        raise NotImplementedError

    def off(self):
        raise NotImplementedError


class LEDController(BaseController):

    def __init__(self, pin: int):
        self.__LED = LED(pin)

    def work_once(self):
        self.__LED.on()
        sleep(1)
        self.__LED.off()

    def on(self):
        self.__LED.on()

    def off(self):
        self.__LED.off()
