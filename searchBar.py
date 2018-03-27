from PyQt5.QtWidgets import QLineEdit

import sql

class searchBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.returnPressed.connect(self.searchForPeople)

    def searchForPeople(self):
        sql.listFromSearch("Justin")
        print("Hello")

