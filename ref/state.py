#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#
from typing import Tuple
from data_source.fr24_crawler import Fr24Crawler
from light_controller.controller import *


class State:

    def __init__(self, loc: Tuple[float, float], rng: float, interval=5):
        self.__loc = loc
        self.__range = rng
        self.__flt_lst = []
        self.__interval = interval
        self.__actions = []
        self.__crawler = Fr24Crawler(loc, rng)

    def get_location(self) -> Tuple[float, float]:
        return self.__loc

    def get_range(self) -> float:
        return self.__range

    def set_location(self, loc: Tuple[float, float]):
        self.__loc = loc

    def set_range(self, rng: float):
        self.__range = rng

    def add_action(self, action: BaseController):
        self.__actions.append(action)

    def spin(self):
        self.add_action(LEDController(17))
        while True:
            try:
                this_data = self.__crawler.get_data_once()
                if this_data:
                    for action in self.__actions:
                        action.work_once()
            except KeyboardInterrupt:
                return

if __name__ == '__main__':
    s = State((0,0), 10000)
    s.spin()
