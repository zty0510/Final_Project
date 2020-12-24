# =============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
# =============================================================================#
from flask import Flask, request, render_template
import csv
import state
import controller
import os

web_server = Flask(__name__)
web_server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@web_server.route('/')
def home():
    return render_template('index.html')


@web_server.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        center_Lon = request.form.get('center_Lon')  # 从form处获取POST信息
        center_Lat = request.form.get('center_Lat')
        northeastern_Lon = request.form.get('northeastern_Lon')
        northeastern_Lat = request.form.get('northeastern_Lat')
        blink_interval = request.form.get('blink_interval')
        crawler_interval = request.form.get('crawler_interval')

        path = os.path.abspath(".") + r"/online_data.csv"  # 获取当前目录绝对路径
        with open(path, "w+") as f:
            f.write("center_Lon,center_Lat,northeastern_Lon,northeastern_Lat,crawler_interval,LED_time")
            f.write("\n")
        with open(path, "a+", newline="") as f:
            writec = csv.writer(f)
            row = [center_Lon, center_Lat, northeastern_Lon, northeastern_Lat, blink_interval, crawler_interval]
            writec.writerow(row)
        crawler = state.State([float(center_Lon), float(center_Lat)],
                              [float(northeastern_Lon), float(northeastern_Lat)])
        crawler.spin(int(crawler_interval), int(blink_interval))


@web_server.route('/config')
def config():
    csvfile = open("online_data.csv", encoding="utf-8")
    content = csv.reader(csvfile)
    rows = [row for row in content]
    data = rows[1]
    center_Lon = data[0]
    center_Lat = data[1]
    northeastern_Lon = data[2]
    northeastern_Lat = data[3]
    blink_interval = data[4]
    crawler_interval = data[5]
    dic = {
        'loc': [center_Lon, center_Lat],
        'rng': [northeastern_Lon, northeastern_Lat],
        'LED_time': (blink_interval),
        'crawler_time': (crawler_interval),
    }
    return render_template('config.html', **dic)


@web_server.route('/showdata')
def showdata():
    csvfile = open("csv_data.csv", encoding="utf-8")
    content = csv.reader(csvfile)
    rows = [row for row in content]
    key = rows[0]
    del rows[0]
    list = []
    for values in rows:
        dic = dict(map(lambda x, y: [x, y], key, values))
        list.append(dic)
    return render_template('showdata.html', data=list)


@web_server.route('/vis', methods=['GET'])
def vis():
    raise NotImplementedError


if __name__ == "__main__":
    web_server.run(debug=True, host="127.0.0.2", port=5000)
