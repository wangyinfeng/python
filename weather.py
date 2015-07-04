# -*- coding: utf-8 -*-
# Learn how to use public API
# 1. Simpfile the code, the icon print is fine, but not beatful, no icons, only words. - DONE
# 2. accept parameter(city and days) from command line.
# 3. select language automatically according to the terminal encoding.
# 4. is it possible to get history data? Do more investigate about the provided API, learn how to use the public API.
# 5. if it's possible to get more data, try analysis the data.
# 6. warp with a gui?
# 7. why so slow?
# 
# Copy from 
# https://github.com/smartczy/weather_py/blob/master/src/weather.py
#
# import requests
import urllib
import json
import sys
from datetime import datetime, timedelta

# The API manual page:
# http://www.worldweatheronline.com/api/docs/local-city-town-weather-api.aspx
base_url = "http://api.worldweatheronline.com/free/v2/weather.ashx"

windDir = {
        "N":   "↓",
        "NNE": "↓",
        "NE":  "↙",
        "ENE": "↙",
        "E":   "←",
        "ESE": "←",
        "SE":  "↖",
        "SSE": "↖",
        "S":   "↑",
        "SSW": "↑",
        "SW":  "↗",
        "WSW": "↗",
        "W":   "→",
        "WNW": "→",
        "NW":  "↘",
        "NNW": "↘",
        }


class Query(object):
    def __init__(self, day, city):
        self.day = day
        self.time = [3,4,5,6]
        self.weatherCode = ''
        self.weather = ''
        self.date = ''
        self.hourly = ''
        self.tempC = 0
        self.winddir16Point = ''
        self.windspeedKmph = 0
        self.humidity = 0
        self.chanceofwater = 0
        self.city = city
        self.visibility = 0
        self.pressure = 0

    def query(self):
    # 使用resquests
    # p={"q":"%s"%self.city, "num_of_days":3, "format":"json", "key":"55f1fdd05fba23be0a18043d0a017", "lang":"zh"}
    # response=requests.get(base_url,params=p)
    # json_string = response.text

    #使用urllib
    #If specified the language, the data will inside member "lang_zh", otherwise will inside weatherDesc
    #url = base_url + "?key=0225e665449eee8612275c9511e11&q=%s&num_of_days=3&format=json&lang=zh" % self.city
        url = base_url + "?key=0225e665449eee8612275c9511e11&q=%s&num_of_days=3&format=json" % self.city

        response = urllib.urlopen(url)
        json_string = response.read()
        parsed_json = json.loads(json_string)
        data = parsed_json['data']

        try:
            self.weather = data['weather'][self.day]
        except KeyError:
            print "Please input the correct city or area name:"
            sys.exit()

        self.date = self.weather['date']

    def detail(self, time):
        self.hourly = self.weather['hourly'][time]           # 获取小时数据，time:100-1500

        self.weatherCode = self.hourly['weatherCode']
        self.tempC = self.hourly['tempC']
        self.winddir16Point = self.hourly['winddir16Point']
        self.windspeedKmph = self.hourly['windspeedKmph']
        self.chanceofrain = self.hourly['chanceofrain']
        self.chanceofsnow = self.hourly['chanceofsnow']
        self.humidity = self.hourly['humidity']
        self.visibility = self.hourly['visibility']
        self.pressure = self.hourly['pressure']
        self.chanceofwater = int(self.chanceofrain) if int(self.chanceofrain) > int(self.chanceofsnow) else int(self.chanceofsnow)
        self.sunrise = self.weather['astronomy'][0]['sunrise']
        self.sunset = self.weather['astronomy'][0]['sunset']
        self.moonrise = self.weather['astronomy'][0]['moonrise']
        self.moonset = self.weather['astronomy'][0]['moonset']

    def printSingle(self):
        l1 = l2 = l3 = l4 = l5 = l6 = ''
        for time in self.time:
            self.detail(time)

            if len(self.hourly['weatherDesc'][0]['value'].encode("utf-8")) <= 8:
                l1 += '|' + self.hourly['weatherDesc'][0]['value'].encode("utf-8") + '\t\t\t'
            elif len(self.hourly['weatherDesc'][0]['value'].encode("utf-8")) > 16:
                l1 += '|' + self.hourly['weatherDesc'][0]['value'].encode("utf-8") + '\t'
            else:
                l1 += '|' + self.hourly['weatherDesc'][0]['value'].encode("utf-8") + '\t\t'

            l2 += '|' + str(self.tempC) + " C"+'\t\t\t'
            l3 += '|' + windDir[self.winddir16Point]+" "+ str(self.windspeedKmph) + "km/h" + '\t\t'
            l4 += '|' + "Rain:" + str(self.chanceofwater) + "%" + '\t\t'
            l5 += '|' + "Humidity:" + str(self.humidity) + "%" + '\t\t'
            l6 += '|' + "Pressure:" + str(self.pressure) + "mb" + '\t'

        print l1+"|"
        print l2+"|"
        print l3+"|"
        print l4+"|"
        print l5+"|"
        print l6+"|"
        print "Visibility:%s" % str(self.visibility)+"km"
        print "Sun rise:%s" % str(self.sunrise)
        print "Sun set:%s" % str(self.sunset)
        print "Moon rise:%s" % str(self.moonrise)
        print "Moon set:%s" % str(self.moonset)

    def printDay(self, delta):
        date_time = datetime.strftime(datetime.today() + timedelta(days=delta),"%Y-%m-%d")
        print "\t\t\t\t\t%s" %date_time
        print "-------------------------------------------------------------------------------------------------"
        print "|        Morning        |         Noon          |         Evening       |        Night          |"
        print "-------------------------------------------------------------------------------------------------"
        self.printSingle()
        print '\n'


def main():
    try:
        city = sys.argv[1]
    except IndexError:
        print "Please input the city or area name:"
        city = raw_input()
        if city == '':
            sys.exit()

#    day = [0,1,2]
    day = [1]
    for i in day:
       query = Query(i,city)
       query.query()
       query.printDay(i)

if __name__ == "__main__":
    main()
