#=============================================================================#
#                              Python Project                                 #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, SubmitField
from wtforms.validators import DataRequired
import fr24_crawler

web_server = Flask(__name__)
web_server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
web_server.secret_key = 'heima'
class InputForm(FlaskForm):
    center_Lon = StringField(u"中心点经度:",validators=[DataRequired()])
    center_Lat = StringField(u"中心点维度:",validators=[DataRequired()])
    northeastern_Lon = StringField(u"西北方经度:",validators=[DataRequired()])
    northeastern_Lat = StringField(u"西北方维度:",validators=[DataRequired()])
    crawler_interval = StringField(u'爬取时间间隔:',validators=[DataRequired()])
    submit = SubmitField(u"提交")




@web_server.route('/',methods=['GET', 'POST'])
def home():

    form = InputForm()
    # 1. 判断请求方式是post
    if request.method == 'POST':
        # 2. 获取请求的参数
        center_Lon = request.form.get('center_Lon')
        center_Lat = request.form.get('center_Lat')
        northeastern_Lon = request.form.get('northeastern_Lon')
        northeastern_Lat = request.form.get('northeastern_Lat')
        crawler_interval = request.form.get('crawler_interval')
        print(center_Lat, center_Lon, northeastern_Lat, northeastern_Lon, crawler_interval)
        print(type(center_Lat))
        crawler = fr24_crawler.Fr24Crawler((float(center_Lon),float(center_Lat)),(float(northeastern_Lon),float(northeastern_Lat)))
        crawler.store_data()
        print(crawler.get_Quantity_Binary_List())

    return render_template("index.html",form = form)

@web_server.route('/config', methods=['GET', 'POST'])
def config():

    raise NotImplementedError


@web_server.route('/vis', methods=['GET'])
def vis():
    raise NotImplementedError



web_server.run(host="127.0.0.1", port=5000)
