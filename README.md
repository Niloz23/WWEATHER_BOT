# Telegram Weather Bot

## Описание проекта

Этот проект представляет собой Telegram-бота, который интегрируется с API OpenWeatherMap и предоставляет пользователям актуальные данные о погоде по названию города. Бот запрашивает информацию у пользователя, отправляет запрос на OpenWeatherMap API и возвращает текущие погодные условия, такие как температура, влажность и краткое описание погоды.

## Функциональные возможности

- Принимает название города от пользователя в Telegram.
- Делает запрос к OpenWeatherMap API для получения данных о текущей погоде.
- Возвращает информацию о температуре, влажности и описание погоды в указанном городе.
- Обрабатывает исключения, связанные с неправильным вводом данных.

### Используемые технологии

- Python 3.9+
- Библиотека [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) для интеграции с Telegram.
- OpenWeatherMap API для получения данных о погоде.
- Библиотека `requests` для выполнения HTTP-запросов.

## Как пользоваться ботом

1. Отправьте название города в чат с ботом, чтобы получить текущие погодные условия в этом городе.
2. Бот вернет данные о температуре (в градусах Цельсия), уровне влажности и краткое описание погоды.

## Условия задачи

Этот проект был выполнен в рамках тестового задания, суть которого заключалась в создании Telegram-бота, интегрированного с API погоды. Вот основные требования задания:

- Бот должен принимать название города от пользователя.
- Бот должен делать запрос к API сервиса погоды (например, OpenWeatherMap).
- Бот должен возвращать информацию о текущей погоде в указанном городе: температура, влажность и описание погодных условий.
- Для разработки можно было использовать Python с библиотеками `aiogram` или `pyTelegramBotAPI` либо Node.js.

## Возможности для доработки

- Добавить поддержку прогноза на несколько дней вперед.
- Добавить поддержку более детализированной информации (скорость ветра, атмосферное давление).
- Внедрить функционал подписки на ежедневные уведомления о погоде в выбранных городах.

# Ссылка на бота в Telegram:
[https://t.me/WWEATHER_FOR_bot](https://t.me/WWEATHER_FOR_bot)


 
