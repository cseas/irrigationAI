import numpy
from flask import Flask
from flask import request
from flask import make_response

from threading import Thread

import rain_predictor
import weatherApi

import json
import time

app = Flask(__name__)
url = ""
ipaddr = ""

meantempm = 0.0
meanpressurem = 0.0
maxhumidity = 0.0
minhumidity = 0.0
maxtempm = 0.0
mintempm = 0.0
precipm = 0.0

moisture = 0.

pumpOnCode = 699
pumpOffCode = 700

returnCode = pumpOffCode


def get_weather_params():
    global meantempm, meanpressurem, maxhumidity, minhumidity, maxtempm, mintempm, precipm, returnCode
    counter = 0    # get data every 5 min. Perform calculations every 30 min.
    while True:
        if counter % 5 == 0:
            temp, pressure, humidity, precipitation = weatherApi.get_params()

            meantempm += temp
            meanpressurem += pressure

            if maxhumidity == 0 or humidity > maxhumidity:
                maxhumidity = humidity
            if minhumidity == 0 or humidity < minhumidity:
                minhumidity = humidity

            precipm += precipitation

        if counter == 30:
            counter = 0
            meantempm /= 3
            meanpressurem /= 3
            if precipm == 0:
                precipm = minhumidity/100
            if rain_predictor.predict(numpy.asarray((meantempm, meanpressurem,
                                                  maxhumidity, minhumidity,
                                                  maxtempm, mintempm, precipm)).reshape(1, -1)) > 0.7:
                returnCode = pumpOnCode
            else:
                returnCode = pumpOffCode

        time.sleep(60*30)
        counter += 1


@app.route('/', methods=['GET', 'POST'])
def what_to_do():
    global url, ipaddr, moisture

    moisture = request.args.get("moisture")
    print(moisture)

    r = make_response(json.dumps({
        "message": moisture
    }))

    return r, returnCode


if __name__ == '__main__':
    weather_fetcher = Thread(name='weatherFetcher', target=get_weather_params())
    weather_fetcher.start()
    app.run(port=8080, host='0.0.0.0')
