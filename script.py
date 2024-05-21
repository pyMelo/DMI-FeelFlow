from pyrogram import Client
from datetime import datetime
import pandas as pd
import time
import os
import dotenv
from typing import Any, List  # Correzione qui


dotenv.load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
channel_id = os.getenv('CHANNEL_ID')
message_id = os.getenv('MESSAGE_ID')

app = Client('session_name', api_id=api_id, api_hash=api_hash)
data_list = []

def connect_client() -> 'bool':
    print('Connecting to client...')
    started = datetime.today()
    app.start()
    print("App started successfully.")
    return app.is_connected

def get_chat_messages(limit: int) -> List[any]:
    i = 0
    chat_history = app.get_chat_history(channel_id, limit=limit)
    for message in chat_history:
        i += 1
        print("\n##### Spot numero: " + str(i) + " ID : " + str(message.id))
        if message.text is not None:
            print(message.text)
            comments = []
            print("\n## Commenti del post con ID :" + str(message.id))
            for reply in app.get_discussion_replies(channel_id, message.id):
                if reply.text is not None:
                    print("- "+reply.text)
                    comments.append(reply.text)
                    time.sleep(2)
            data_list.append({
                "Message ID": message.id,
                "Spot": message.text,
                "Comments": comments
            })
        elif message.caption:
            print(" ------------- Text of the Spot ------------------- ")
            print(message.caption)
            data_list.append({
                "Message ID": message.id,
                "Spot": message.caption,
                "Comments": []
            })
    return data_list

def end_app() -> 'bool':
    app.stop()
    print("App stopped.")
    return app.is_connected

def create_csv() -> None:
    df = pd.DataFrame(data_list)
    df.to_csv("data.csv", index=False)
    print("CSV created successfully.")

def main():
    connection_status = connect_client()
    if connection_status:
        limit = int(input("Enter the limit for retrieving chat messages: "))
        get_chat_messages(limit)
        create_csv_option = input("Do you want to create a CSV file? (yes/no): ").lower()
        if create_csv_option == "yes":
            create_csv()
        end_app()
    else:
        print("Failed to connect to client.")

if __name__ == "__main__":
    main()