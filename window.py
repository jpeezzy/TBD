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
                             QGridLayout, QLineEdit,
                             QWidgetItem)
from PyQt5.QtGui import (QIcon, QFont)
import sql
class mainWindow(QWidget):
    # Personal Informatiion page variables
    information = ['First' , 'Middle',
                   'Last', 'Client Relationship',
                   'Phone', 
                   'Address', 
                   'Birth Date',
                   'Client Name', 
                   'School',
                   'Grade'
                   ]

    def __init__(self):
        super().__init__()
        #Initializing all our widgets and lbales for our class
        self.nameFirst = QLabel(self.information[0])
        self.middleFirst = QLabel(self.information[1])
        self.firstEdit = QLineEdit()
        self.middleEdit = QLineEdit()
        #send in buttons
        self.submitButton = QPushButton('Submit', self);
        self.submitButton.resize( \
                                 self.submitButton.sizeHint())

        #intialize grids for all pages 
        self.gridUserInformation = QGridLayout()

        #End initialization and begin the UI
        self.initUI()

    def initUI(self):
        #Setting up Fonts
        QToolTip.setFont(QFont('Times', 10))

        #Initialize Grid 
        self.gridUserInformation.setSpacing(6)
        self.setLayout(self.gridUserInformation)

        #Call Function to add our initlalized widgets into the grid
        self.addUserInfoWidget(self.gridUserInformation)

        #window settings 
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.submitButton.move(250, 500)
        self.show()

    #This function sets up the personal information of the 
    #current customer
    def addUserInfoWidget(self, grid):
        #add information to grid
        grid.addWidget(self.nameFirst, 1,0)
        grid.addWidget(self.middleFirst, 1,2)
        self.firstEdit = QLineEdit();
        self.middleEdit = QLineEdit();
        grid.addWidget(self.firstEdit, 1,1)
        grid.addWidget(self.middleEdit, 1,3)
        self.firstEdit.setReadOnly(False)
        self.middleEdit.setReadOnly(False)
        positions = [(i,j) for i in range(6) for j in range(1)]
        for i in range(2,8):
            if self.information[i] == '':
                continue
            editForm = QLineEdit()
            InfoLabel = QLabel(self.information[i], self)
            grid.addWidget(InfoLabel, i, 0)
            grid.addWidget(editForm, i, 1)
            #editForm.setReadOnly(False)

            #add buttons here
            grid.addWidget(self.submitButton, 8,1)
        return
    #end add information 

    #Sends the information from the sql function
    #To the screen on an empty user template. The list
    #format is as follows:
    #First, Middle, Last, Client relaitonship, phone, address,
    #Birth Date, Client name
    #def addInformation(self, First, middle, last, 
    #                   clientRelation, PhoneNum, address,  
    #                   birthDate, nameOfClient, school, grade):

    def addInformation(self, infoList):
        self.firstEdit.setText(infoList[0]);
        self.middleEdit.setText(infoList[1]);
        self.firstEdit.setReadOnly(True)
        self.middleEdit.setReadOnly(True)
        for i in range(2,8):
            if self.information[i] == '':
                continue
            #Adds the other necessary information 
            textEditTemp = self.gridUserInformation.itemAtPosition(i,1)
            textEditTemp.widget().setText(infoList[i])
            textEditTemp.widget().setReadOnly(True)


    #Method: singUPinfo:
    #adds user information to the sql database from a gui
    def signUP(self):
        self.addUserInfoWidget(self.gridUserInformation);



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    sqlperson = ["Justin", "dongil", "Lee", "bro",
                 "1234", "234234", "0330", "sa", "NOGALES",
                 "11"]
    #window.addInformation(sqlperson)
    listTest = sql.getPersonalInformation("6268270307")
    #convert the list[0]tuple to juts a list
    #window.addInformation(list(listTest[0]))
    window.signUP()
    #sql.listFromSearch("Justin")

    sys.exit(app.exec_())
