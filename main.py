from modules.transferM import *
from modules.start import *
from modules.history import *
from modules.blik import *
from modules.info import *
import pymysql as p
import sys,os, time



def menu(number):
    while True:
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            print("Nie udało połączyć się z bazą danych")
            time.sleep(2)
            sys.exit()
        cursor = myBase.cursor()

        #checking balance
        cursor.execute("SELECT balance FROM data WHERE number={}".format(number))
        accountBalanceB = cursor.fetchall()
        for ch in accountBalanceB:
            for v in ch:
                accountBalance=v
        os.system("cls")
        print("===============")
        print("     MENU")
        print("===============")
        print()
        print("Stan konta: ", accountBalance, "zl")
        print("1. Przelew")
        print("2. Historia przelewow")
        print("3. Blik")
        print("4. Informacje o koncie")
        print("5. Wyjscie")
        ch = input("Wybor: ")
        if ch == "1":
            cursor.close()
            myBase.close()
            transfer(number)
        elif ch == "2":
            cursor.close()
            myBase.close()
            history(number)
        elif ch == "3":
            cursor.close()
            myBase.close()
            blik()
        elif ch == "4":
            cursor.close()
            myBase.close()
            info(number)    
        elif ch == "5":
            os.system("cls")
            print("ZEGNAMY")
            time.sleep(2)
            sys.exit()
            cursor.close()
            myBase.close()
        else:
            print("Nie ma takiej opcji")
            time.sleep(2)

    #close connecting
    cursor.close()
    myBase.close()


welcome()
number = authentication()
for ch in number:
    for v in ch:
        number=v
menu(number)