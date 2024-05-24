"""Modulo che esegue la sentiment di alcuni spot del canale telegram dmi"""
import time
import os
from typing import List
import dotenv
from pyrogram import Client
import pandas as pd

dotenv.load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
channel_id = os.getenv('CHANNEL_ID')
message_id = os.getenv('MESSAGE_ID')

app = Client('session_name', api_id=api_id, api_hash=api_hash)
data_list = []

def connect_client() -> 'bool':
    """Modulo che esegue la connessione del client."""
    print('Connecting to client...')
    app.start()
    print("App started successfully.")
    return app.is_connected

def get_chat_messages(limit: int) -> List[any]:
    """Modulo che prende n messaggi del channel dmi."""
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
    """Modulo che stoppa il client."""
    app.stop()
    print("App stopped.")
    return app.is_connected

def create_csv() -> None:
    """Modulo che crea il csv con gli spot e la sentiment."""
    df = pd.DataFrame(data_list)
    df.to_csv("data.csv", index=False)
    print("CSV created successfully.")

def main():
    """Modulo main che lancia tutte le function definite in precedenza."""
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
