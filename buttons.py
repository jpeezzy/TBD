from PyQt5.QtWidgets import (QPushButton)

class buttons:
    def __init__(self):
    #def initButtonforUserInfo(self):
        #send in buttons for tab1 (userinfo)
        self.submitButton = QPushButton('Submit');
        self.submitButton.resize(self.submitButton.sizeHint())
        self.editButton = QPushButton('edit');
