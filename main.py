import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


def log(message, answer):
    from datetime import datetime
    print('\n----------')
    print(datetime.now())
    print("Message from {0} {1}. {id = {2}}\n text: {3}".format(message.from_user.first_name,
                                                                message.from_user.last_name,
                                                                str(message.from_user.id),
                                                                message.text))
    print(answer)


@bot.message_handler(content_types=['text'])  # Функция обрабатывает текстовые сообщения
def send_message(message):
    answer = 'I am replying to your text'
    log(message, answer)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
