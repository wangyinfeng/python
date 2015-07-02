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
    "N":   "\033[1m↓\033[0m",
    "NNE": "\033[1m↓\033[0m",
    "NE":  "\033[1m↙\033[0m",
    "ENE": "\033[1m↙\033[0m",
    "E":   "\033[1m←\033[0m",
    "ESE": "\033[1m←\033[0m",
    "SE":  "\033[1m↖\033[0m",
    "SSE": "\033[1m↖\033[0m",
    "S":   "\033[1m↑\033[0m",
    "SSW": "\033[1m↑\033[0m",
    "SW":  "\033[1m↗\033[0m",
    "WSW": "\033[1m↗\033[0m",
    "W":   "\033[1m→\033[0m",
    "WNW": "\033[1m→\033[0m",
    "NW":  "\033[1m↘\033[0m",
    "NNW": "\033[1m↘\033[0m",
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

        def query(self):
                # 使用resquests
                # p={"q":"%s"%self.city, "num_of_days":3, "format":"json", "key":"55f1fdd05fba23be0a18043d0a017", "lang":"zh"}
                # response=requests.get(base_url,params=p)
                # json_string = response.text

                #使用urllib
                url = base_url + "?key=0225e665449eee8612275c9511e11&q=%s&num_of_days=3&format=json&lang=zh" % self.city
                
                response = urllib.urlopen(url)
                json_string = response.read()
                parsed_json = json.loads(json_string)
                data = parsed_json['data']              # 获取所有数据

                try:
                        self.weather = data['weather'][self.day]            # 获取天气预报,[]内０代表当天,1代表明天，以此类推。
                except KeyError:
                        print "\033[1;31;49m" + "请输入正确的城市或地区！" + "\033[0m"
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
                self.chanceofwater = int(self.chanceofrain) if int(self.chanceofrain) > int(self.chanceofsnow) else int(self.chanceofsnow)

        def printSingle(self):
                l1 = l2 = l3 = l4 = l5 = ''
                for time in self.time:
                        self.detail(time)

                        l1 += '│' + self.hourly['lang_zh'][0]['value'].encode("utf-8") + '\t\t' if len(self.hourly['lang_zh'][0]['value'].encode("utf-8")) <= 9 else '│' + self.hourly['lang_zh'][0]['value'].encode("utf-8") + '\t'
                        l2 += '│' + temp_color(self.tempC) + "°C"+'\t\t'
                        l3 += '│' + windDir[self.winddir16Point]+" "+ wind_color(self.windspeedKmph) + "km/h" + '\t'
                        l4 += '│' + "降水概率:" + str(self.chanceofwater) + "%" + '\t'
                        l5 += '│' + "湿度:" + str(self.humidity) + "%" + '\t'

                print l1+"│"
                print l2+"│"
                print l3+"│"
                print l4+"│"
                print l5+"│"

        def printDay(self, delta):
                date_time = datetime.strftime(datetime.today() + timedelta(days=delta),"%Y-%m-%d")
                line1 = "                         ┌─────────────┐                                 "
                line2 = "┌───────────────┬───────────%s──────────┬───────────────┐" % date_time
                line3 = "│  Morning      │   Noon └──────┬──────┘ Evening│     Night     │"
                line4 = "├───────────────┼───────────────┼───────────────┼───────────────┤"
                endline="└───────────────┴───────────────┴───────────────┴───────────────┘"
                print line1
                print line2
                print line3
                print line4
                self.printSingle()
                print endline

def temp_color(temp):
        if temp >= 35 or temp <= -10:
                color = "\033[1;31;49m" + str(temp) + "\033[0m"
        elif (temp >= 25 and temp <35):
                color = "\033[1;33;49m" + str(temp) + "\033[0m"
        elif temp > 10 and temp < 25:
                color = "\033[1;32;49m" + str(temp) + "\033[0m"
        elif temp >-10 and temp <= 10:
                color = "\033[1;34;49m" + str(temp) + "\033[0m"
        return color
def wind_color(windspeed):
        if windspeed <= 5:
                color = "\033[1;32;49m" + str(windspeed) + "\033[0m"
        elif windspeed > 5 and windspeed <=10:
                color = "\033[1;33;49m" + str(windspeed) + "\033[0m"
        else:
                color = "\033[1;34;49m" + str(windspeed) + "\033[0m"
        return color

def main():
        try:
                city = sys.argv[1]
        except IndexError:
                print "\033[1;31;49m" + "Please input the city or area name" + "\033[0m"
                city = raw_input()
                if city == '':
                        sys.exit()
        day = [0,1,2]
        for i in day:
                query = Query(i,city)
                query.query()
                query.printDay(i)

if __name__ == "__main__":
        main()
