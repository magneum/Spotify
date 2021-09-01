import os
import time
import logging
os.system("pip install python-telegram-bot==12.3.0")
os.system("pip install spotdl==3.7.2")
os.system("clear")
import telegram.ext as tg
from telegram.ext import MessageHandler, Filters



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)




updater = tg.Updater(
token = "1940504180:AAGg7L53zq9oZgxqeHrfkc4x0nHcrTAzG_0",
workers=200,
use_context=True)
dispatcher = updater.dispatcher




def get_single_song(bot, update):
    chat_id = update.effective_message.chat_id
    message_id = update.effective_message.message_id

    url = "'" + update.effective_message.text + "'"

    os.system(f'mkdir -p .temp{message_id}{chat_id}')
    os.chdir(f'./.temp{message_id}{chat_id}')

    FET = bot.send_message(
    chat_id=chat_id,
    text="Fetching...")
    os.system(f'spotdl {url}')


    time.sleep(1)
    FET.delete()
    

    try:
        sent = 0 
        SE = bot.send_message(
        chat_id=chat_id,
        text="Sending to You...")




        files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(".") for f in filenames if os.path.splitext(f)[1] == '.mp3']
        for file in files:
            bot.send_audio(chat_id=chat_id, audio=open(f'./{file}', 'rb'), timeout=1000)
            sent += 1
        


        SE.delete()
    except:
        pass


    os.chdir('./..')
    os.system(f'rm -rf .temp{message_id}{chat_id}')



    if sent == 0:
        bot.send_message(
        chat_id=chat_id,
        text="It seems there was a problem in finding/sending the song.")
    else:
        logging.info("Sent Audio")

            

        

handler = MessageHandler(
Filters.text,
get_single_song)
dispatcher.add_handler(
handler=handler)
updater.start_polling()
updater.idle()