from datetime import datetime
import pytest
from unittest.mock import MagicMock
import script

data_list = []

@pytest.fixture
def mock_client(pytest_mock):
    client = MagicMock()
    client.is_connected = False  # Mock the is_connected property to prevent connection attempts
    client.connect = MagicMock()  # Mock the connect method to prevent connection attempts
    client.load_session = MagicMock()  # Mock the load_session method to prevent session loading
    client.storage.open = MagicMock()  # Mock the storage.open method to prevent file operations

    pytest_mock.patch("script.Client", return_value=client)  # Patch the Client class to return the mock client
    
    return client

data_list = []

def test_start_client(mock_client):  
    assert script.connect_client() == True

def test_getChatMessages(mock_client): 
    assert script.get_chat_messages(2) != []


def test_getChatMessagesFormat(mock_client):
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


