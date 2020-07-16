#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from gpiozero import LED as _LED
from time import sleep as _sleep
import multiprocessing


class BaseController:

    def __init__(self):
        raise NotImplementedError

    def work_once(self, flight_list):
        raise NotImplementedError

    def on(self):
        raise NotImplementedError

    def off(self):
        raise NotImplementedError


class LEDController(BaseController):

    def __init__(self, pin: int):
        self.__LED = _LED(pin)
        self.__process = None

    def work_once(self, flight_list):
        self.__LED.on()
        _sleep(1)
        self.__LED.off()

    @staticmethod
    def _work(freq, led):
        t = 1 / freq
        while True:
            led.on()
            _sleep(t)
            led.off()

    def on(self, flight_list):
        if self.__process:
            return
        self.__process = multiprocessing.Process(
            target=LEDController._work, args=(1, self.__LED))
        self.__process.start()

    def off(self):
        if not self.__process:
            return
        self.__process.terminate()
