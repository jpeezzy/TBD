from PyQt5.QtWidgets import QLineEdit

import sql

class searchBar(QLineEdit):
    def __init__self(self):
        super().__init__()

    def searchForPeople(self):
        sql.listFromSearch("Justin")
        print("Hello")

