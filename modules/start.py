import time, os, sys
import pymysql as p


def welcome():
    print("-------------\nWitamy w BBP\n-------------")
    time.sleep(2)
    os.system("cls")


def authentication():
    #Create empty tuple
    temp = ()
    #Connect with data base
    try:
        myBase=p.connect(host="localhost", user="root", db="bank")
    except:
        print("Nie udało się połączyć z bazą danych")
        time.sleep(2)
        sys.exit()
    cursor = myBase.cursor()
    
    for i in range(4):
        j = 3 - i
        login=input("Wprowadz login: ")
        password=input("Wprowadz hasło: ")
        if j == 0:
            print("Blokowanie konta")
            time.sleep(2)
            cursor.close()
            myBase.close()
            sys.exit()
        cursor.execute("SELECT login FROM data WHERE login in ('{}')".format(login))
        loginB=cursor.fetchall()
        if loginB !=temp:
            cursor.execute("SELECT password FROM data WHERE password in ('{}')".format(password))
            passwordB=cursor.fetchall()
            if passwordB !=temp:
                cursor.execute("SELECT number FROM data WHERE login in ('{}')".format(login))
                number=cursor.fetchall()
                os.system("cls")
                print("Logowanie...")
                time.sleep(2)
                os.system("cls")
                cursor.close()
                myBase.close()
                return number
            else:
                print("Złe hasło")
                time.sleep(2)
                os.system("cls")
        else:
            print("Zły login")
            time.sleep(2)
            os.system("cls")
    #close connecting
    cursor.close()
    myBase.close()