import os
import logging
from telegram.ext import Updater, MessageHandler, Filters
logging.basicConfig(
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
level=logging.INFO)
runner = Updater("1940504180:AAGg7L53zq9oZgxqeHrfkc4x0nHcrTAzG_0")
dispatcher = runner.dispatcher
def VOID_FEEDER(client, update):
    VOID_ID = update.effective_message.chat_id
    message_id = update.effective_message.message_id
    url = """ + update.effective_message.text + """
    os.system(f"mkdir -p .hypespoted{message_id}{VOID_ID}")
    os.chdir(f"./.hypespoted{message_id}{VOID_ID}")
    os.system(f"spotdl {url}")
    DONE = 0 
    S = client.send_message(chat_id=VOID_ID,text="Sending")
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(".") for f in filenames if os.path.splitext(f)[1] == ".mp3"]
    for file in files:
        client.send_audio(chat_id=VOID_ID, audio=open(f"./{file}", "rb"), timeout=500)
        DONE += 1
    os.chdir("./..")
    os.system(f"rm -rf .hypespoted{message_id}{VOID_ID}")
    S.delete()
    if DONE == 0:
       client.send_message(chat_id=VOID_ID,
       text="Error! Check link or report @HypeVoids")
    else:
        pass
VOID_DONE = MessageHandler(Filters.text,VOID_FEEDER)
dispatcher.add_handler(handler=VOID_DONE)
runner.start_polling(poll_interval=0.8)
runner.idle()