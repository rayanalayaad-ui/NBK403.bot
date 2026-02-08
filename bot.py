import telebot
import requests
import os
from flask import Flask
import threading

# --- [ إعدادات الهوية ] ---
TOKEN = "حط_التوكن_هنا"
CHAT_ID = "حط_الايدي_هنا"
ACCESS_CODE = "NBK403"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
user_status = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔐 أدخل رمز الوصول (Access Code):")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id
    if str(chat_id) != str(CHAT_ID):
        bot.send_message(chat_id, "❌ غير مخول.")
        return
    if chat_id not in user_status or not user_status[chat_id]:
        if message.text == ACCESS_CODE:
            user_status[chat_id] = True
            msg = "⚠️ NBK403 ONLINE ⚠️\n/ip - فحص السيرفر\n/phish - الروابط"
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "❌ خطأ.")
        return
    if message.text == "/ip":
        ip = requests.get('https://api.ipify.org').text
        bot.send_message(chat_id, f"🌐 IP: {ip}")
    elif message.text == "/phish":
        bot.send_message(chat_id, "🔗 الرابط: https://nbk403-reaper-bot.onrender.com")

@app.route('/')
def index():
    return "NBK403 is Active"

def run_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

