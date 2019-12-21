import pymysql as p
import time, sys, os

def info(number):
    os.system("cls")
    #Connect with data base
    try:
        myBase = p.connect(host="localhost", user="root", db="bank")
    except:
        print("Nie udało połączyć się z bazą danych")
        time.sleep(2)
        sys.exit()
    cursor = myBase.cursor()

    #import login
    cursor.execute("SELECT login FROM data WHERE number = {}".format(number))
    loginT=cursor.fetchall()
    for ch in loginT:
        for v in ch:
            login=v
    #import password
    cursor.execute("SELECT password FROM data WHERE number = {}".format(number))
    passwordT=cursor.fetchall()
    for ch in passwordT:
        for v in ch:
            password=v
    #import pin
    cursor.execute("SELECT pin FROM data WHERE number = {}".format(number))
    pinT=cursor.fetchall()
    for ch in pinT:
        for v in ch:
            pin=v
    #import balance
    cursor.execute("SELECT balance FROM data WHERE number = {}".format(number))
    balanceT=cursor.fetchall()
    for ch in balanceT:
        for v in ch:
            balance=v
    #import name
    cursor.execute("SELECT name FROM data WHERE number = {}".format(number))
    nameT=cursor.fetchall()
    for ch in nameT:
        for v in ch:
            name=v
    #import surname
    cursor.execute("SELECT surname FROM data WHERE number = {}".format(number))
    surnameT=cursor.fetchall()
    for ch in surnameT:
        for v in ch:
            surname=v
    #import dateOfBirth
    cursor.execute("SELECT dateOfBirth FROM data WHERE number = {}".format(number))
    dateOfBirthT=cursor.fetchall()
    for ch in dateOfBirthT:
        for v in ch:
            dateOfBirth=v
    #import accountNumber
    cursor.execute("SELECT accountNumber FROM data WHERE number = {}".format(number))
    accountNumberT=cursor.fetchall()
    for ch in accountNumberT:
        for v in ch:
            accountNumber=v

    print("============================================")
    print("Login: ", login)
    print("Hasło: ", password)
    print("Pin: ", pin)
    print("Stan konta: ", balance)
    print("Imie: ", name)
    print("Nazwisko: ", surname)
    print("Data urodzenia: ", dateOfBirth)
    print("Numer konta: ", accountNumber)
    print("============================================")
    input()
