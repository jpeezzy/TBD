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
                             QGridLayout)
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
        self.setLayout(grid)

        information = ['Name' , 'Middle',
                       'Last', 'Client Relationship',
                       'Phone', 
                       'Address', 
                        'Birth Date',
                       'Client Name', 
                       'School',
                       'Grade'
                       ]
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, info in zip(positions, information):
            if info == '':
                continue
            InfoLabel = QLabel(info, self)
            grid.addWidget(InfoLabel, *position)


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
