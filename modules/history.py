import os, time, sys
import pymysql as p

def history(number):
    os.system("cls")
    theDate=[]
    accountNumber=[]
    amount=[]
    comment=[]
    
    #Connect with data base
    try:
        myBaseH = p.connect(host="localhost", user="root", db="bank")
    except:
        print("Nie udało połączyć się z bazą danych")
        time.sleep(2)
        sys.exit()
    cursor = myBaseH.cursor()
    
    try:
        #Import date
        cursor.execute("SELECT date FROM `{}`".format(number))
        dateB = cursor.fetchall()
        for ch in dateB:
            for v in ch:
                theDate.append(v)
        
        #Import accountNumber
        cursor.execute("SELECT accountNumber FROM `{}`".format(number))
        accountNumberB = cursor.fetchall()
        for ch in accountNumberB:
            for v in ch:
                accountNumber.append(v)
        #Import amount
        cursor.execute("SELECT amount FROM `{}`".format(number))
        amountB = cursor.fetchall()
        for ch in amountB:
            for v in ch:
                amount.append(v)
        #Import comment
        cursor.execute("SELECT comment FROM `{}`".format(number))
        commentB = cursor.fetchall()
        for ch in commentB:
            for v in ch:
                comment.append(v)
        #Import counter
        cursor.execute("SELECT COUNT(*) FROM `{}`".format(number))
        counterB=cursor.fetchall()
        for ch in counterB:
            for v in ch:
                counter=v
    except:
        print("Historia jest pusta")
        time.sleep(2)
        return
    #Print history
    for i in range(counter):
        print("--------------------------------")
        print("Przelew nr ", i+1)
        print("Data: ", theDate[i])
        print("Adres: ", accountNumber[i])
        print("Kwota: ", amount[i], "zł")
        print("Komentarz: ", comment[i])
        print("--------------------------------")
    input()
