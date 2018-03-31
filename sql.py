import json
import sqlite3
from pprint import pprint

conn = sqlite3.connect('Guardian.db')
c = conn.cursor()

def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS Guardian(fname TEXT, middle TEXT, last TEXT, clientRelation TEXT, Phone TEXT, Address TEXT, DOB TEXT, ClientName TEXT, school TEXT, grade TEXT)')

def dataEntry(fname, middle, last, clientRelation, PHONE, ADDRESS, \
              DOB, ClientName, school, Grade):
    c.execute("INSERT INTO Guardian(fname, middle, last, clientRelation, Phone, Address, "\
              "DOB, ClientName, school, grade) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (fname, middle, last, clientRelation, PHONE, ADDRESS, DOB, ClientName, school, Grade)) 
    conn.commit()
   # c.close()
   # conn.close()

#Function listFromSearch(name)
#This function should give a list if you type in someone's name 
# input : name of the Guardian 
# output : list of all people with the same name, but also show their kid
# looking after in the program as well as their birthdate. 
def listFromSearch(Guardian): 
    c.execute('SELECT {col1},{col2},{col3},{col4},{col5},{col6},{col7}\
              FROM {tn} WHERE {cn}="{Name}"'.\
              format(col1 = "fname",col2 = "middle", col3 = "last", col4="DOB", col5= "Phone", 
                     col6="Address", col7="ClientName", 
                     tn="Guardian", cn="fname", Name = Guardian))
    all_rows = c.fetchall()
    #print('2):', all_rows)
    return all_rows

#This function will get the entire row based on an identification (probably phone number) 
def getPersonalInformation(ID):
    c.execute('SELECT * \
              FROM {tn} WHERE {cn}="{NUMBER}"'.\
              format(tn = "Guardian", cn = "Phone", NUMBER = ID))
    all_rows = c.fetchall()
    #print('2):', all_rows)
    return all_rows
    information
    return information

'''
createTable()
name = "Justin"
clientRelation = "bro"
phone = "6268270307"
address = "2602 east "
DOB = "03/30/1997"
ClientName = "SH"
school = "SUZANNE"
grade = "12"
'''
#creating a testBench usikng the file dataSet.json (has 100 entries for testing) 
def testBench():
    createTable()
    data = json.load(open('dataSet.json'))
    for i in range (0,100):
        namef = data["data"][i][0]
        middle = data["data"][i][1]
        last = data["data"][i][2]
        cR = data["data"][i][3] #client relation
        pN = data["data"][i][4] # number
        aD = data["data"][i][5] # address
        dob = data["data"][i][6] # date of birth
        cName = data["data"][i][7] # client Name
        sCH = data["data"][i][8] #school client goes to
        gR = data["data"][i][9]  # grade
        dataEntry(namef, middle, last, cR, pN, aD, dob, cName, sCH, gR)
        #for j in range(0,8):
            #print(data["data"][i][j],end=" ")
        #print("")
    #pprint(data)


#dataEntry(name, clientRelation, phone, address, \
#          DOB, ClientName, school, grade)

#listFromSearch("Justin")
# 2) Value of a particular column for rows that match a certain value in column_1


