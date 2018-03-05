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

#Function listFromSearch(name)
#This function should give a list if you type in someone's name 
# input : name of the Guardian 
# output : list of all people with the same name, but also show their kid
# looking after in the program as well as their birthdate. 
def listFromSearch(Guardian): 
    c.execute('SELECT {col1},{col2},{col3},{col4},{col5}\
              FROM {tn} WHERE {cn}="{Name}"'.\
              format(col1 = "name", col2="DOB", col3= "Phone", 
                     col4="Address", col5="ClientName", 
                     tn="Guardian", cn="name", Name = Guardian))
    all_rows = c.fetchall()
    print('2):', all_rows)
    return all_rows

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

#listFromSearch("Justin")
# 2) Value of a particular column for rows that match a certain value in column_1


