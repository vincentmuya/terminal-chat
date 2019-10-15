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

    '''
    This function handles loginto the system. In a real world app, you might need ti connect ti API's or database to verify users
    '''
    def login(self):
        username = input("Please enter your username:")
        password = getpass.getpass("Please enter %s's Password" % username)
        if username in self.users:
            if self.users[username] == password:
                self.user = username
            else:
                print(colored("Your password is incorrect", "red"))
                self.login()
        else:
            print(colored("Your username is incorrect", "red"))
            self.login()
