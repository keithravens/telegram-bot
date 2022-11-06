import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello'])
def greet(message):
  bot.reply_to(message, 'Heyo bro')

@bot.message_handler(commands=['sendmsg'])
def sendmsg(message):
  bot.send_message(message.chat.id, str(f"Bleh {message.chat.id}"))
  
def msgfrmtext(msg):
  if msg=="heyo":
    pass
  bot.send_message(msg.chat.id,msg.text)
@bot.message_handler(func=msgfrmtext)
def funcreplysender(message):
  pass

bot.polling()
