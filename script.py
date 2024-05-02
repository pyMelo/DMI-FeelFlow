from pyrogram import Client
from datetime import datetime
import pandas as pd
import time
import os
import dotenv

dotenv.load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
channel_id = os.getenv('CHANNEL_ID')
message_id = os.getenv('MESSAGE_ID')

app = Client('session_name', api_id=api_id, api_hash=api_hash)
data_list = []

def connetticlient():
    started = datetime.today()
    app.start()
    print(" ######## app started successfully ########### ")
    return app.is_connected



# connetticlient()