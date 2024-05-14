import pytest
from datetime import datetime
import script

data_list = []

def test_start_client():  
    assert script.connect_client() == True

def test_getChatMessages(): 
    assert script.get_chat_messages(2) != []


def test_getChatMessagesFormat():
    data_list = script.get_chat_messages(10)
    for item in data_list:
        assert "Message ID" in item
        assert "Spot" in item
        assert "Comments" in item
        assert isinstance(item["Message ID"], int)
        assert item["Message ID"] >= 0
        assert isinstance(item["Spot"], str) or item["Spot"] is None
        assert isinstance(item["Comments"], list) or item["Comments"] is None



def session_ended():
    assert script.end_app() == False



# def prova():
#     script.connect_client()
#     data_list = script.get_chat_messages(10)
#     for item in data_list:
#         print(item)

# prova()