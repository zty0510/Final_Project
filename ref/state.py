#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#
import logging
from typing import Tuple
from time import sleep
from os.path import exists
from simplejson import load, dump
from data_source.fr24_crawler import Fr24Crawler
from light_controller.controller import *

_config_location = '/tmp/fly_over.json'
_logger = logging.getLogger("WFO-Cralwer")
_logger.setLevel('INFO')


class State:

    def __init__(self):
        self.__config_location = _config_location
        self.__flt_lst = []
        self.__actions = []
        self.__update_config()
        _logger.warning("Cralwer initalized.")

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

    def __update_config(self):
        with open(self.__config_location) as f:
            config = load(f)
            self.__loc = (config['long'], config['lati'])
            self.__range = config['rng']
            self.__interval = config['interval']
            self.__crawler = Fr24Crawler(self.__loc, self.__range)
            self.__actions = []
            # self.add_action(LEDController(17))

    def spin(self):
        while True:
            try:
                self.__flt_lst = self.__crawler.get_data_once()
                _logger.info("Get flight list of {} flights.".format(
                    len(self.__flt_lst)))
                if self.__flt_lst:
                    for action in self.__actions:
                        action.work_once(self.__flt_lst)
                self.__update_config()
                sleep(self.__interval)
            except KeyboardInterrupt:
                return


if __name__ == '__main__':
    default_config = {
        "freq": 1.0,
        "long": 0.0,
        "lati": 0.0,
        "rng": 1.0,
        "interval": 5.0
    }
    if not exists(_config_location):
        with open(_config_location, mode="w+") as f:
            dump(default_config, f)
    s = State()
    s.spin()
