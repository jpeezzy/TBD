import sqlite3

conn = sqlite3.connect('Guardian.db')
c = conn.cursor()

def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS Guardian(name TEXT, clientRelation TEXT, Phone TEXT, Address TEXT, DOB TEXT, ClientName TEXT, school TEXT, grade TEXT)')

def dataEntry(name, clientRelation, PHONE, ADDRESS, \
              DOB, ClientName, school, Grade):
    c.execute("INSERT INTO Guardian(name, clientRelation, Phone, Address, "\
              "DOB, ClientName, school, grade) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
        (name, clientRelation, PHONE, ADDRESS, DOB, ClientName, school, Grade)) 
    conn.commit()
   # c.close()
   # conn.close()

createTable()
name = "Justin"
clientRelation = "bro"
phone = "6268270420"
address = "2602 east "
DOB = "03/30/1997"
ClientName = "SH"
school = "SUZANNE"
grade = "12"
dataEntry(name, clientRelation, phone, address, \
          DOB, ClientName, school, grade)
