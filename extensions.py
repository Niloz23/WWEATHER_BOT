import requests
from config import OWM_API_KEY


class APIException(Exception):
    pass


class WeatherAPI:
    @staticmethod
    def get_weather(city: str):
        try:
            # Формируем запрос к API OpenWeatherMap
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=ru'
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                raise APIException(f"Город {city} не найден.")

            # Извлекаем нужные данные из ответа
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']

            return temperature, humidity, weather_desc

        except Exception as e:
            raise APIException(f"Ошибка при получении данных о погоде: {e}")
