#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QApplication, QToolTip,
                             QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QLineEdit)
from PyQt5.QtGui import (QIcon, QFont)

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        #Setting up Fonts and buttons 
        QToolTip.setFont(QFont('Times', 10))
        submitButton = QPushButton('Submit', self);
        submitButton.resize( \
            submitButton.sizeHint())

        #Initialize Grid 
        grid = QGridLayout()
        grid.setSpacing(6)
        self.setLayout(grid)
        
        information = ['First' , 'Middle',
                       'Last', 'Client Relationship',
                       'Phone', 
                       'Address', 
                        'Birth Date',
                       'Client Name', 
                       'School',
                       'Grade'
                       ]

        #add information to grid
        nameFirst = QLabel(information[0])
        middleFirst = QLabel(information[1])
        grid.addWidget(nameFirst, 1,0)
        grid.addWidget(middleFirst, 1,2)
        firstEdit = QLineEdit()
        middleEdit = QLineEdit()
        grid.addWidget(firstEdit, 1,1)
        grid.addWidget(middleEdit, 1,3)
        firstEdit.setReadOnly(True)
        middleEdit.setReadOnly(True)
        positions = [(i,j) for i in range(6) for j in range(1)]
        for i in range(2,8):
            if information[i] == '':
                continue
            editForm = QLineEdit()
            InfoLabel = QLabel(information[i], self)
            grid.addWidget(InfoLabel, i, 0)
            grid.addWidget(editForm, i, 1)
            editForm.setReadOnly(True)

        grid.addWidget(submitButton, 8,1)
        #Setting up Message Boxes and it's font
        '''nameLabel = QLabel('Name', self)
        nameLabel.setFont(QFont("Times", 10))
        nameLabel.move(200,200)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(nameLabel)
        hbox.addWidget(submitButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)'''

        #Set the parameters of the window
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        submitButton.move(250, 500)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
