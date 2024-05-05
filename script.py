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

def connetticlient() -> None:
    started = datetime.today()
    app.start()
    print(" ######## app started successfully ########### ")
    return app.is_connected

def getChatMessages() -> None:
    i = 0
    chat_history = app.get_chat_history(channel_id, limit=100,offset_id=16108)
    for message in chat_history:
        i+=1
        
        # A) Possibility to get the posts with images AND video and getting the text under written. 
        if message.text is None:
            print("\n##### Spot numero: " + str(i) + " ID : " + str(message.id))

            if message.photo:
                print(" ------------- Image of the Spot ------------------- ")
                # A) Download the images/video on the "downloads" directory.
                # image = app.download_media(message.photo.file_id,f'image{message.id}.jpg')
                # print(image)
            if message.video:
                print(" ------------- Video of the Spot ------------------- ")
                # video = app.download_media(message.video.file_id,f'video{message.id}.mp4')
                # print(video)  
                if message.caption:
                    print(" ------------- Text of the Spot ------------------- ")
                    text_below = message.caption
                    print(message.caption)
            
        if message.text is not None:
            print("\n##### Spot numero: " + str(i) + " ID : " + str(message.id))
            print(message.text)
            comments = []
            print("\n## Commenti del post con ID :" + str(message.id))
            for reply in app.get_discussion_replies(channel_id, message.id):
                
                # Q) Not sure if is saving the corret file, not visible from my laptop.
                
                # if reply.text is None:         
                #     if reply.animation:
                #         print(" ------------- GIF of the comment ------------------- ")
                #         gif = app.download_media(reply.animation.file_id,f'animation{reply.id}.gif')
                #         print(gif)
                #     if reply.sticker:
                #         print(" ------------- Sticker of the comment ------------------- ")
                #         sticker = app.download_media(reply.sticker.file_id,f'sticker{reply.id}.jpeg')
                #         print(sticker)
                
                    # A) Added the same concept as the post.
                    if reply.photo:
                        print(" ------------- Image of the comment ------------------- ")
                        # A) Download the images/video on the "downloads" directory.
                        image = app.download_media(reply.photo.file_id,f'image{reply.id}.jpg')
                        print(image)
                    if reply.video:
                        print(" ------------- Video of the comment ------------------- ")
                        video = app.download_media(reply.video.file_id,f'video{reply.id}.mp4')
                        print(video)
                        
                        if reply.caption:
                            print(" ------------- Text of the comment ------------------- ")
                            text_below = reply.caption
                            print("- "+ message.caption)
            
            # A) If the message doesn't contain text it doesn't enter in the if (None = GIF,STICKER,PHOTO,VIDEO,VOICE MESSAGE(?) ).
            if reply.text is not None:
                print("- "+reply.text)
                comments.append(reply.text)
                time.sleep(2)
                
            data_list.append({
                "Message ID": message.id,
                "Spot": message.text,
                "Comments": comments
            })

def appEnd() -> None:
    app.stop()
    return app.is_connected
    
def creazioneCSV() -> None:
    df = pd.DataFrame(data_list)
    df.to_csv("data.csv", index=False)

# connetticlient()
#getChatMessages()