from PyQt5.QtWidgets import (QTabWidget, QWidget,
                             QGridLayout)


class tabs(QTabWidget):
    def __init__(self):
        # Initialize tab screen
        super().__init__()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.resize(300,200) 
 
        # Add tabs tab1 will be user profile,
        self.addTab(self.tab1,"User Profile")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Programs")
        self.addTab(self.tab4,"History")

        #set tab layout
        self.tab1.layout = QGridLayout()
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.layout.setSpacing(6)
