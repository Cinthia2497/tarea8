import telebot
bot = telebot.TeleBot('1944409495:AAF0imcyfhSfdZMPGKhBBdMkDH788SUAN3I') 
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola']) 
def hola(mensaje):
    bot.reply_to(mensaje, "Hola")

@bot.message_handler(commands=['celsius']) 
def hola(mensaje):
    bot.reply_to(mensaje, "K = ºC + 273.15.")
    
@bot.message_handler(commands=['kelvin']) 
def hola(mensaje):
    bot.reply_to(mensaje, "ºC = K – 273.15")
    
bot.polling()