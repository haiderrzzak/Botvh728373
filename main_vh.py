import os
import telebot
from flask import Flask, request

# توكن البوت
TOKEN = '7184192457:AAGQVu-ruj70nUPqLtjySKmvqZAeFbZHuhA'
bot = telebot.TeleBot(TOKEN)

# إعداد Flask
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def home():
    return "Webhook set to..."  # للتأكد أن التطبيق يعمل

if __name__ == "__main__":
    app.run(debug=True)
