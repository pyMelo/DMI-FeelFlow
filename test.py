import pytest
from datetime import datetime
import script

def test_start_client():  
    assert script.connetticlient() == True

def test_getChatMessages(): 
    assert script.getChatMessages2(2) != []


def test_getChatMessagesFormat():
    data_list = script.getChatMessages2(limit=100)
    for item in data_list:
        assert "Message ID" in item
        assert "Spot" in item
        assert "Comments" in item
        assert isinstance(item["Message ID"], int)
        assert item["Message ID"] >= 0
        assert isinstance(item["Spot"], str) or item["Spot"] is None
        assert isinstance(item["Comments"], list) or item["Comments"] is None



def session_ended():
    assert script.appEnd() == False