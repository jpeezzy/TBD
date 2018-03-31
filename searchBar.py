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
        for _x in searchList:
            #add each result from the list to the widget
            for _y in range(0,6):
                _line = QTableWidgetItem()
                _line.setText(_x[_y])
                self._tableTest.setItem(_i,_y,_line)
                #to make sure it's read only
                _line.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            _i+=1
            #print(_x)
        searchTab.layout.addWidget(self._tableTest)
