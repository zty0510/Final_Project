#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#
from typing import Tuple
from data_source.fr24_crawler import Fr24Crawler
from light_controller.controller import LEDController


class State:

    def __init__(self: State, loc: Tuple[float, float], rng: float, interval=5):
        self.__loc = loc
        self.__range = rng
        self.__flt_lst = []
        self.__interval = interval
        self.__actions = []

    def get_location(self) -> Tuple[float, float]:
        return self.__loc

    def get_range(self) -> float:
        return self.__range

    def set_location(self, loc: Tuple[float, float]):
        raise NotImplementedError

    def set_range(self, rng: float):
        raise NotImplementedError

    def add_action(self, actions):
        raise NotImplementedError

    def spin(self):
        raise NotImplementedError
