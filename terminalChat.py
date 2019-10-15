from pusher import Pusher
import pysher
import os
import json
import getpass
from temcolor import colored
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

class terminalChat():
    pusher = None
    channel = None
    chatroom= None
    clientPusher = None
    user = None
    users = {
        "samuel": "samuel'spassword",
        "daniel": "daniel'spassword",
        "tobi": "tobi'spassword",
        "sarah": "sarah'spassword"

    }
    chatrooms =["sports", "general", "education", "health", "technology"]

    '''
    The entry point of the application
    '''
    def main(self):
        self.login()
        self.selectChatroom()
        while True:
            self.getInput()
