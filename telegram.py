import telebot
from telebot import types
import os
#

def main():
    bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
    chat_id = os.environ['CHAT_ID']
    text = "New Pull Request created! Check it out: " + os.environ['GITHUB_SERVER_URL'] + '/' + os.environ['GITHUB_REPOSITORY'] + '/pull/' + os.environ['GITHUB_REF'].split('/')[2]
    bot.send_message(chat_id, text)


if __name__ == '__main__':
    main()
