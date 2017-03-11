from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    print('Вызван/start', print(update))
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def help_user(bot, update):
    bot.sendPhoto(update.message.chat_id, photo = 'http://www.sunny-cat.ru/datas/users/1-kenny005.jpg')

def talk_to_me(bot,update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, text = 'Dont know')

def show_error(bot, update, error):
    print(error)

def main():
    updater = Updater('316197946:AAFIUvoyrd3ZvTFJbvJAj0GIZ3gAw8C6ods')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('help', help_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)
    

    updater.start_polling()
    updater.idle()

main()