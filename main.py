import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import config

bot = telebot.TeleBot(config.TOKEN)


def log(message, answer):
    from datetime import datetime
    print('\n----------')
    print(datetime.now())
    print("Message from {0} {1}. id = {2}\n text: {3}".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id),
                                                              message.text))
    print(answer)


@bot.message_handler(content_types=['text'])  # Функция обрабатывает текстовые сообщения
def send_message(message):
    answer = 'Choose'
    log(message, answer)

    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(InlineKeyboardButton(text='DevOps', callback_data='1'))
    inline_keyboard.add(InlineKeyboardButton(text='QA tester', callback_data='2'))
    inline_keyboard.add(InlineKeyboardButton(text='Developer', callback_data='3'))
    bot.send_message(message.chat.id, answer, reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    answer = 'default'
    if call.message:
        if call.data == '1':
            answer = 'Option 1 selected'
        elif call.data == '2':
            answer = 'Option 2 selected'
        elif call.data == '3':
            answer = 'Option 3 selected'
    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True)
