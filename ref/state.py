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
import numpy as np
import matplotlib.pyplot as plt
from light_controller.controller import *
import matplotlib
matplotlib.use('Agg')

_config_location = '/tmp/fly_over.json'
_graph_location = 'web_server/static/'
_logger = logging.getLogger("WFO-Cralwer")
_logger.setLevel('INFO')

plt.rcParams['xtick.labelsize'] = 6


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
            # self.__actions = []
            # self.add_action(LEDController(17))

    def __draw(self):
        if not self.__flt_lst:
            return
        carrier = {}
        for flt in self.__flt_lst:
            if not flt.get("flight"):
                continue
            try:
                carrier[flt['flight'][0:2]] += 1
            except:
                carrier[flt['flight'][0:2]] = 1
        carrier_lst = sorted(list(carrier.keys()))
        carrier_cnt = [carrier[k] for k in carrier]
        x_axis = np.arange(len(carrier_lst))
        plt.bar(tuple(x_axis), carrier_cnt,
                align='center', alpha=0.5)
        plt.xticks(x_axis, carrier_lst, rotation=90)
        plt.ylabel("Number")
        plt.xlabel("Carrier")
        plt.title("Flight Number by Carrier")
        plt.savefig("{}/carrier.png".format(_graph_location))
        plt.clf()

    def spin(self):
        while True:
            try:
                self.__flt_lst = self.__crawler.get_data_once()
                _logger.info("Get flight list of {} flights.".format(
                    len(self.__flt_lst)))
                if self.__flt_lst:
                    self.__draw()
                    for action in self.__actions:
                        action.work_once(self.__flt_lst)
                self.__update_config()
                sleep(self.__interval)
            except KeyboardInterrupt:
                return


if __name__ == '__main__':
    default_config = {
        "freq": 1.0,
        "long": 30.0,
        "lati": 104.0,
        "rng": 100000.0,
        "interval": 5.0
    }
    if not exists(_config_location):
        with open(_config_location, mode="w+") as f:
            dump(default_config, f)
    s = State()
    s.spin()
