#=============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from typing import List, Tuple, Dict, Any
import requests
import csv
import time
import json
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup
import  re

class Fr24Crawler:

    def __init__(self, loc: Tuple[float, float], rng: float):
        # lon: 经度
        # lat:纬度
        self.loc=loc
        self.rng=rng


        # raise NotImplementedError


    def get_square(self):
        # jdc = abs(self.loc[1] - self.rng[1])  # 计算经度差
        # if jdc > 180:  # 经度差调整
        #     jdc = 360 - jdc
        #
        # maxlon = self.loc[1] + jdc
        # minlon = self.loc[1] - jdc
        # if minlon < -180:
        #     minlon = minlon + 360
        #
        # ans = sorted([maxlon, minlon])
        # minlon1 = ans[0]
        # maxlon1 = ans[1]
        #
        # # 经度计算
        #
        # wdc = abs(self.rng[0] - self.loc[0])
        # minlat = self.loc[0] - wdc
        # maxlat = self.loc[0] + wdc
        #
        # if maxlat > 90 or minlat < -90:
        #     print("illegal")
        if not (-180 <= self.loc[1] <= 180 and -90 <= self.loc[0] <= 90):
            raise ValueError("请输入正确的经纬度")

        jdc = abs(self.loc[1] - self.rng[1])  # 计算经度差
        if jdc < 180:
            if self.loc[1] < 0:
                if self.rng[1] > 0:  # 去除rng在loc的东侧
                    raise ValueError('rng应该在loc的西侧')
        if jdc > 180:  # 经度差调整
            if self.loc[1] > 0:
                if self.rng[1] < 0:  # 去除rng在loc的东侧
                    raise ValueError('rng应该在loc的西侧')
            else:
                jdc = 360 - jdc
        if self.loc[1] < 0:
            maxlon = self.loc[1] - jdc
            minlon = self.loc[1] + jdc
            if maxlon <= -180:  # 180度不分东西经
                maxlon = maxlon + 360
        if self.loc[1] > 0:
            maxlon = self.loc[1] + jdc
            minlon = self.loc[1] - jdc
            if maxlon > 0:
                maxlon = maxlon - 360

        ans = sorted([maxlon, minlon])
        minlon1 = ans[0]
        maxlon1 = ans[1]

        # 经度计算

        wdc = abs(self.rng[0] - self.loc[0])
        minlat = self.loc[0] - wdc
        maxlat = self.loc[0] + wdc

        if minlat<-90:           #若最小纬度越界，构不成方形
            raise ValueError("最小纬度越界")

        return ([minlon1, maxlon1, minlat, maxlat])


    def get_data_once(self,updated_token):
        square_param = self.get_square()#获取所需查询面积的参数（经纬度）
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': '* / *',
            'Referer': 'https: // zh.flightaware.com / live /',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh - CN, zh;q = 0.9, en - US;q = 0.8, en;q = 0.7'
        }
        base_url = 'https://zh.flightaware.com/ajax/vicinity_aircraft.rvt?'
        token = updated_token  # 未来需要对token的更新进行处理
        param = '&minLon={minLon}&minLat={minLat}&maxLon={maxLon}&maxLat={maxLat}&token={token}'.format\
            (minLon=square_param[0],maxLon=square_param[1],minLat=square_param[2],maxLat=square_param[3],token=token)#  序列化参数
        url = base_url + param  #得到最终的请求url
        print(url)
        response = requests.get(url=url,headers=headers)
        return json.loads(response.text)




    def spin(self, interval=1):
        while True:
            self.store_data()
            time.sleep(interval)
        raise NotImplementedError




    def get_updated_token(self):
        req = requests.get("https://zh.flightaware.com/live/")
        token = re.findall("VICINITY_TOKEN\":\"(.*?)\"", req.text)#从html中提取新的TOKEN
        return token[0]

    def store_data(self):
        data_source = self.get_data_once(updated_token=self.get_updated_token())#得到新的token并传入，爬取数据
        #遍历 data，并做空值判断以及数据处理

        for i in range(1,len(data_source['features'])):
            if 'coordinates' not in data_source['features'][i]["geometry"]:
                data_source['features'][i]["geometry"]['coordinates']=None
            else :
                latitude = data_source['features'][i]["geometry"]['coordinates'][0]
                longitude = data_source['features'][i]["geometry"]['coordinates'][1]
            if 'direction' not in data_source['features'][i]["properties"]:
                heading = None
            else:
                heading = data_source['features'][i]["properties"]['direction']
            if 'altitude' not in data_source['features'][i]["properties"]:
                altitude = None
            else:
                altitude = data_source['features'][i]["properties"]['direction']
            if 'groundspeed' not in data_source['features'][i]["properties"]:
                groundspeed = None
            else:
                groundspeed = data_source['features'][i]["properties"]['groundspeed']
            if 'flight_number' not in data_source['features'][i]["properties"]:
                flight_number = None
            else:
                flight_number = data_source['features'][i]["properties"]['ident']

            # heading = data_source['features'][i]["properties"]['direction']
            #             # altitude = data_source['features'][i]["properties"]['altitude']
            #             # groundspeed = data_source['features'][i]["properties"]['groundspeed']
            #             # flight_number = data_source['features'][i]["properties"]['ident']
            departure_airport_IATA_CODE = data_source['features'][i]["properties"]['origin']['iata']
            arrival_airport_IATA_CODE = data_source['features'][i]["properties"]['destination']['iata']
            print(f'第{i}架飞机\n'
                f'Latitude(经度):{latitude}\n'
                  f'Longitude(纬度):{longitude}\n'
                  f'heading(航向）:{heading}\n'
                  f'altitude(海拔高度）:{altitude}\n'
                  f'groundspeed(地速):{groundspeed}\n'
                  f'flight_number(航班号):{flight_number}\n'
                  f'departure_airport_IATA_CODE(离开地机场代码):{departure_airport_IATA_CODE}\n'
                  f'arrival_airport_IATA_CODE(抵达机场代码):{arrival_airport_IATA_CODE}\n\n\n\n\n'
            )
            # print(latitude,longitude,heading,altitude,groundspeed,flight_number,departure_airport_IATA_CODE,arrival_airport_IATA_CODE)





a = Fr24Crawler((-50,29),(-25,20))
a.spin(interval=5)