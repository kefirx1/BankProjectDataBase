from modules.transferM import *
from modules.start import *
from modules.history import *
from modules.blik import *
import sys,os, time

def menu():
    global accountBalance
    while True:
        os.system("cls")
        print("===============")
        print("     MENU")
        print("===============")
        print()
        print("Stan konta: ", accountBalance, "zl")
        print("1. Przelew")
        print("2. Historia przelewow")
        print("3. Blik")
        print("4. Wyjscie")
        ch = input("Wybor: ")
        if ch == "1":
            accountBalance=transfer(historyOfTTemp, accountBalance)
        elif ch == "2":
            history(historyOfT)
        elif ch == "3":
            blik()
        elif ch == "4":
            # saving account balance
            accountBalanceTxtS = open("data/stanKonta.data", "wt", encoding="UTF-8")
            accountBalanceTxtS.write(str(accountBalance))
            accountBalanceTxtS.close()
            sys.exit()
        else:
            print("Nie ma takiej opcji")
            time.sleep(2)


# opening data
try:
    accountBalanceTxt =  open("data/stanKonta.data", "rt", encoding="utf-8")
    accountBalanceS = accountBalanceTxt.readline()
    accountBalance = float(accountBalanceS)
    historyOfTTxt = open("data/przelewy.data", "rt", encoding="utf-8")
    historyOfT = historyOfTTxt.readlines()
except:
    print("Nie udało się połączyć z bazą danych")
    time.sleep(3)
    sys.exit()

# variables
historyOfTTemp = []  # temp for transfer history

welcome()
authentication()
menu()

