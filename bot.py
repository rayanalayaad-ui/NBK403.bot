import telebot
import requests
import os
from flask import Flask

# --- [ إعدادات الهوية - تأكد من تعبئتها ] ---
TOKEN = "8394691279:AAHSo6NSEbIdIp2XQx5WsMHf418-t24ilPs" 
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
    # التحقق من أنك أنت فقط صاحب الايدي اللي يقدر يستخدم البوت
    if str(chat_id) != str(CHAT_ID): 7119607904
        bot.send_message(chat_id, "❌ أنت غير مخول لاستخدام هذا البوت.")
        return

    if chat_id not in user_status or not user_status[chat_id]:
        if message.text == ACCESS_CODE:
            user_status[chat_id] = True
            bot.send_message(chat_id, "✅ تم التفعيل! المنظومة جاهزة.\n/phish - توليد روابط\n/ip - فحص السيرفر")
        else:
            bot.send_message(chat_id, "❌ الرمز خطأ.")
        return

    if message.text == "/ip":
        ip = requests.get('https://api.ipify.org').text
        bot.send_message(chat_id, f"🌐 IP السيرفر: {ip}")

@app.route('/')
def index(): return "NBK403 Running"

def run_bot(): bot.polling(none_stop=True)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
