from PyQt5.QtWidgets import QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore
import sql

class searchBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self._tableTest = QTableWidget()

    def searchForPeople(self, searchList, searchTab):
        searchTab.layout.removeWidget(self._tableTest)
        self._tableTest = QTableWidget()
        self._tableTest.setColumnCount(6)
        self._tableTest.setRowCount(10)
        #Resize colums stretch to fit
        self._tableTest.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        _i = 0
        #first initialize the first column
        for _x in searchList:
            #add each result from the list to the widget
            _column1 = QTableWidgetItem()
            _column2 = QTableWidgetItem()
            _column3 = QTableWidgetItem()
            _column4 = QTableWidgetItem()
            _column5 = QTableWidgetItem()
            _column6 = QTableWidgetItem()
            _column1.setText("First Name")
            _column2.setText("Last Name")
            _column3.setText("Phone")
            _column4.setText("Client Relationship")
            _column5.setText("Client Name")
            _column6.setText("Client School")
            self._tableTest.setItem(0,0,_column1)
            self._tableTest.setItem(0,1,_column2)
            self._tableTest.setItem(0,2,_column3)
            self._tableTest.setItem(0,3,_column4)
            self._tableTest.setItem(0,4,_column5)
            self._tableTest.setItem(0,5,_column6)
            _column1.setFlags(QtCore.Qt.ItemIsEnabled)
            _column2.setFlags(QtCore.Qt.ItemIsEnabled)
            _column3.setFlags(QtCore.Qt.ItemIsEnabled)
            _column4.setFlags(QtCore.Qt.ItemIsEnabled)
            _column5.setFlags(QtCore.Qt.ItemIsEnabled)
            _column6.setFlags(QtCore.Qt.ItemIsEnabled)
            for _y in range(0,6):
                _line = QTableWidgetItem()
                _line.setText(_x[_y])
                self._tableTest.setItem(_i+1,_y,_line)
                #to make sure it's read only
                _line.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            _i+=1
            #print(_x)
        searchTab.layout.addWidget(self._tableTest)
