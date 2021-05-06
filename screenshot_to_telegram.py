import schedule
import time
from datetime import datetime
import pyscreenshot
import telegram

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

bot = telegram.Bot(token="BOT_TOKEN_HERE")
chat_id = "-TELEGRAM_GROUP_ID_HERE"

def job(t):
	im = pyscreenshot.grab()
	im.save("screen.png", "PNG")
	try:
		bot.send_photo(chat_id=chat_id, photo=open('screen.png', 'rb'))
	except Exception as e:
		print(e)
	return

schedule.every().day.at("09:00").do(job,"")
schedule.every().day.at("10:05").do(job,"")
schedule.every().day.at("11:11").do(job,"")

while True:
    schedule.run_pending()
    time.sleep(60)
