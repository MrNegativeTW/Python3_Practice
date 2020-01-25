import json
import urllib.request


def getWeather():
    weatherRawInfo = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Pingtung&appid=4bd72a4d3a28f977a15d5bb1888dad51&units=metric')
    weatherParse = json.load(weatherRawInfo)
    tempMin = weatherParse['main']['temp_min']
    tempMax = weatherParse['main']['temp_max']
    print('最低溫: ' + str(tempMin) + '\n最高溫: ' + str(tempMax))

def getAirQuality():
    #TW170116A0203408
    aqRawInfo = urllib.request.urlopen('')
    aqParse = json.load(aqRawInfo)
    pm25 = aqParse[]
    print(pm25)

if __name__ == '__main__':
    getWeather()