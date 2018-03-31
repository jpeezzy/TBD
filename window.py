#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Creator: Justin Lee
#Simple database recorder using PYQT5

import sys
from PyQt5.QtWidgets import (QApplication, QToolTip,
                             QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QLineEdit,
                             QWidgetItem, QTabWidget)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import (pyqtSlot, Qt)

from buttons import buttons
from searchBar import searchBar
import sql
from tabs import tabs

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
        #initialize button
        self.userButtons = buttons() 
        #initiaalzise tabs
        self.tabs = tabs()
        #setup Search bar
        self.searchBarLabel = searchBar()
        self.searchBarLabel.returnPressed.connect(self.searchForPeople)
        #End initialization and begin the UI
        self.initUI()


    def searchForPeople(self):
        _searchTabIndex = 4
        #go to the search tab
        self.tabs.setCurrentIndex(_searchTabIndex)
        #Get the list of people
        _list = sql.listFromSearch(self.searchBarLabel.displayText())
        #in searchBar.py searches for the people and returns a QTableWidget
        self.searchBarLabel.searchForPeople(_list, self.tabs.tab5)
        #After iterate through the list we have
        return _list

    def initUI(self):
        #Setting up Fonts
        QToolTip.setFont(QFont('Times', 10))

        #Initialize Grid
        #self.setLayout(self.gridUserInformation)
        self.layout = QVBoxLayout(self)
        #adding searchbar to widget as well as tabs
        self.layout.addWidget(self.searchBarLabel, 0, Qt.AlignRight | Qt.AlignTop)
        self.layout.addWidget(self.tabs)
        self.addUserInfoWidget(self.tabs.tab1.layout)
        self.setLayout(self.layout)
        #Call Function to add our initlalized widgets into the grid
        #self.addUserInfoWidget(self.gridUserInformation)

        #window settings 
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Toph DataBase')
        self.setWindowIcon(QIcon('web.png'))
        self.userButtons.submitButton.move(250, 500)
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
            grid.addWidget(self.userButtons.submitButton, 8,1)
            grid.addWidget(self.userButtons.editButton, 8,2)
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
            textEditTemp = self.tabs.tab1.layout.itemAtPosition(i,1)
            textEditTemp.widget().setText(infoList[i])
            textEditTemp.widget().setReadOnly(True)


    #Method: singUPinfo:
    #adds user information to the sql database from a gui
    def signUP(self):
        #self.addUserInfoWidget(self.gridUserInformation);
        self.addUserInfoWidget(self.tabs.tab1.layout);



if __name__ == '__main__':
    #initializng testbench
    sql.testBench()
    #done initializing testbench
    app = QApplication(sys.argv)
    window = mainWindow()
    '''sqlperson = ["Justin", "dongil", "Lee", "bro",
                 "1234", "234234", "0330", "sa", "NOGALES",
                 "11"]'''
    #window.addInformation(sqlperson)
    listTest = sql.getPersonalInformation("6268270307")
    #convert the list[0]tuple to juts a list
    #window.addInformation(list(listTest[0]))
    #print(sql.listFromSearch("Justin"))
    window.signUP()
    #sql.listFromSearch("Justin")

    sys.exit(app.exec_())
