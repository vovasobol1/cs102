import requests
from config import weatherApiToken
import datetime


def getWeather(city , weatherApiToken):
    # создадим обьект в котором будем по ключу получать описание погоды
    DisrWeathers = {
        'Clear' : "ясно ",
        'Clouds' : 'облачно ',
        'Rain' : 'дождь ',
        'Drizzle' : 'дождь ' ,
        "Thunderstorm": 'гроза ' ,
        "Snow": "Снег " ,
        'Mist': 'Туман '
    }

    # попытка отправить запрос
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherApiToken}&units=metric'
        )
        # получили ответ с сервера (обьекст json)
        data = r.json()

        # получаем описание погоды
        weaterDiscription = data['weather'][0]['main']
        # если описание погоды совпадает с одним из ключей обьекта мы запишем в переменную смайлик
        # иначе поместим в переменную универсальный ответ
        if weaterDiscription in DisrWeathers :
            strWeatherDiscr = DisrWeathers[weaterDiscription]
        else :
            strWeatherDiscr = "выгляни в окно , я не знаю что там за погода !"

        city = data['name']# получим название города из ответа
        curWeather = data['main']['temp']# получение градусов
        humidity = data['main']['humidity']# влажность
        pressure = data["main"]["pressure"] #давление
        windSpeed = data['wind']['speed']# скорость ветра
        # время рассвета и заката получаем (оно изначально в формате unix timestamp)
        sunriseTime = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunriseTime = str(sunriseTime).split()[1] # отделяем время от даты
        # время заката
        sunsetTime = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        sunsetTime = str(sunsetTime).split()[1]  # отделяем время от даты
        return (
              f"погода в {city} \n{strWeatherDiscr}\n"
              f"температура воздуха : {curWeather}°\n"
              f"влажность :{humidity}% \n"
              f"скорость ветра : {windSpeed}м/с \n"
              f"давление :{pressure}мм \n"
              f"рассвет: {sunriseTime} \n"
              f"закат: {sunsetTime} \n"
              )
    except Exception as ex :
        print(ex)
        return 'Не удалось получить информацию о погоде. Пожалуйста, проверьте название города.'


def main():
    city = input('введите город: ')
    print(getWeather(city , weatherApiToken))


if __name__ == '__main__':
    main()

  