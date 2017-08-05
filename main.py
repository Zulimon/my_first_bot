import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='281446968:AAF3wWkjOmvnhkRkxYmrBC7DbkGqV_R2R-c')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def reply(bot, update):
    user_said=update.message.text
    if user_said=="Hola":
        bot_say="Hey!"
    elif user_said=="Qué tal?":
        bot_say="Bien, y tú?"
    else:
        bot_say="Sorry, no te entiendo"
    bot.send_message(chat_id=update.message.chat_id, text=bot_say)

def main:

    echo_handler = MessageHandler(Filters.text, reply)
    dispatcher.add_handler(echo_handler)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()