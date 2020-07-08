#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from typing import List, Tuple, Dict, Any
from math import asin, sqrt, pow, sin, cos, pi
import requests
import logging

_FR24_API_URL = "https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds={},{},{},{}&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1"
_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"


class Fr24Crawler:

    def __init__(self, loc: Tuple[float, float], rng: float):
        self.__loc = loc
        self.__range = rng
        self.__square = loc[0] + sqrt(rng) / 100, loc[0] - \
            sqrt(rng) / 100, loc[1] + sqrt(rng) / 100, loc[1] - sqrt(rng) / 100

    @staticmethod
    def _coord2dist(pa, pb):
        def deg2rad(x): return (180 / pi) * x
        pa = deg2rad(pa[0]), deg2rad(pa[1])
        pb = deg2rad(pb[0]), deg2rad(pb[1])
        a = pa[0] - pb[0]
        b = pa[1] - pb[1]
        return 2 * 6371 * asin(sqrt(pow(sin(a/2), 2) + cos(pa[0]) * cos(pb[0]) * pow(sin(b/2), 2)))

    def get_data_once(self):
        result = requests.get(_FR24_API_URL.format(
            self.__square[0], self.__square[1], self.__square[2], self.__square[3]), headers={"User-Agent": _USER_AGENT})
        planes = []
        if result.ok:
            logging.info("crawlFR24: data got from flightradar24.")
            result = result.json()
            for item in result:
                if isinstance(result[item], list):
                    for i in range(len(result[item])):
                        if result[item][i] == '':
                            result[item][i] = None
                # print(result[item])
                    thisPlane = {}
                    if len(result[item]) >= 19:
                        thisPlane['longtitude'] = result[item][1]
                        thisPlane['latitude'] = result[item][2]
                        thisPlane['heading'] = result[item][3]
                        thisPlane['alititude'] = result[item][4]
                        thisPlane['groundSpeed'] = result[item][5]
                        thisPlane['squawk'] = result[item][6]
                        thisPlane['flightType'] = result[item][8]
                        thisPlane['registration'] = result[item][9]
                        thisPlane['depature'] = result[item][11]
                        thisPlane['destination'] = result[item][12]
                        thisPlane['flight'] = result[item][13]
                        planes.append(thisPlane)
        else:
            logging.warning(
                "crawlFR24: can't get data from flightradar24, returning empty data.")
        return [p for p in planes if self._coord2dist(self.__loc, (p['longtitude'], p['latitude'])) < self.__range]

if __name__ == '__main__':
    c = Fr24Crawler((0,0), 10000)
    print(c.get_data_once())
