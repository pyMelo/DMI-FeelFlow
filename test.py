from datetime import datetime
import pytest
from unittest.mock import MagicMock
import script

# Your existing test fixture
@pytest.fixture
def mock_client(mocker):
    client = mocker.MagicMock()
    client.is_connected = False
    client.connect = mocker.AsyncMock()
    client.load_session = mocker.AsyncMock()
    client.storage.open = mocker.AsyncMock()

    mocker.patch("script.Client", return_value=client)
    
    return client

def test_start_client(mock_client):  
    assert script.connect_client(mock_client) == True

def test_getChatMessages(mock_client): 
    assert script.get_chat_messages(mock_client, 2) != []

def test_getChatMessagesFormat(mock_client):
    data_list = script.get_chat_messages(mock_client, 10)
    # Your assertions here


