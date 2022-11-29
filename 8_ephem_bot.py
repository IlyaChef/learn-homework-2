"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import datetime

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

planet_dict = {
        'Mercury': ephem.Mercury(datetime.now()), 
        'Venus': ephem.Venus(datetime.now()), 
        'Mars': ephem.Mars(datetime.now()), 
        'Jupiter': ephem.Jupiter(datetime.now()),
        'Saturn': ephem.Saturn(datetime.now()),
        'Uranus': ephem.Uranus(datetime.now()),
        'Neptune': ephem.Neptune(datetime.now()),
}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Приветсвуем тебя, любитель астрономии! Мы приоткроем тебе тайны космоса")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def constellation_today(update, context):
    planet_name = update.message.text.split()[1]
    ephem_body = planet_dict.get(planet_name, None)
    if ephem_body!=None:
        constellation = ephem.constellation(planet_dict[planet_name])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Я не знаю такой планеты!')




def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_today))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()




if __name__ == "__main__":
    main()
