from flask import Flask, request, render_template, redirect, url_for
from simplejson import dump, load, dumps
from os.path import exists

web_server = Flask(__name__)

default_config = {
    "freq": 1.0,
    "long": 0.0,
    "lati": 0.0,
    "rng": 1.0,
    "interval": 5.0
}
config_location = '/tmp/fly_over.json'
if not exists(config_location):
    with open(config_location, mode="w+") as f:
        dump(default_config, f)


@web_server.route('/')
def home():
    return render_template('index.html', config=url_for('config'), vis=url_for('vis'))


@web_server.route('/config', methods=['GET', 'POST'])
def config():
    with open(config_location) as f:
        config = load(f)
    if request.method == "GET":
        return render_template('config.html', config=dumps(config))
    elif request.method == "POST":
        for key in config:
            try:
                if len(request.form[key]) > 0:
                    config[key] = float(request.form[key])
            except Exception as e:
                return render_template('config.html', error="Error processing config item `{}`: {}".format(key, e)), 400
        with open(config_location, mode="w") as f:
            dump(config, f)
        return render_template('config.html', config=dumps(config))


@web_server.route('/vis', methods=['GET'])
def vis():
    return


if __name__ == "__main__":
    web_server.run(host="0.0.0.0", port=8999)
