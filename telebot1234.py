import telebot
from config import TOKEN
from extensions import WeatherAPI, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы узнать погоду, введите название города в следующем формате:\n'
            '<название города>.\n'
            'Пример: Москва')
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_weather(message: telebot.types.Message):
    try:
        city = message.text.strip()  # Получаем название города
        if not city:
            raise APIException('Вы не указали город.')

        # Получаем данные о погоде
        temperature, humidity, weather_desc = WeatherAPI.get_weather(city)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос:\n{e}')

    else:
        # Формируем ответ пользователю
        text = (f'Погода в городе {city}:\n'
                f'Температура: {temperature}°C\n'
                f'Влажность: {humidity}%\n'
                f'Описание: {weather_desc}')
        bot.send_message(message.chat.id, text)


bot.polling()
