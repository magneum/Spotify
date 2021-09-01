import os
import logging
os.system("clear")
from telegram.ext import Updater, MessageHandler, Filters
logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)
runner = Updater("1940504180:AAGg7L53zq9oZgxqeHrfkc4x0nHcrTAzG_0")
dispatcher = runner.dispatcher
def get_single_song(bot, update):
    chat_id = update.effective_message.chat_id
    message_id = update.effective_message.message_id
    url = "'" + update.effective_message.text + "'"
    os.system(f'mkdir -p .temp{message_id}{chat_id}')
    os.chdir(f'./.temp{message_id}{chat_id}')
    logging.log(logging.INFO, f'start downloading')
    os.system(f'spotdl {url}')
    logging.log(logging.INFO, 'sending to client') 
    sent = 0 
    bot.send_message(chat_id=chat_id, text="Sending to You...")
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(".") for f in filenames if os.path.splitext(f)[1] == '.mp3']
    for file in files:
        bot.send_audio(chat_id=chat_id, audio=open(f'./{file}', 'rb'), timeout=1000)
        sent += 1
    os.chdir('./..')
    os.system(f'rm -rf .temp{message_id}{chat_id}')
    if sent == 0:
       bot.send_message(chat_id=chat_id,
       text="It seems there was a problem in finding/sending the song.")
    else:
        pass
handler = MessageHandler(Filters.text, get_single_song)
dispatcher.add_handler(handler=handler)
runner.start_polling(poll_interval=0.8)
runner.idle()