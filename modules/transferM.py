import os, time

def transfer(historyOfTTemp, accountBalance):
    historyOfTTemp.clear()
    os.system("cls")
    print("Stan konta: ", accountBalance, "zl")
    nrOfT = int(input("Numer konta odbiorcy: "))
    howMuch = float(input("Podaj kwote przelewu: "))
    com = input("Komentarz do przelewu: ")
    back = input("Anuluj(tak/nie): ")
    if back == "tak":
        os.system("cls")
        print("Anulowanie... ")
        time.sleep(2)
        return accountBalance
    elif back == "nie":
        if howMuch > accountBalance:
            print("Kwota przelewu: ", howMuch, "jest wieksza niz stan konta: ", accountBalance)
            time.sleep(2)
            return accountBalance
        print("Wysylanie przelewu pod numer: ", nrOfT, ", o kwocie: ", howMuch, " zl", " , z komentarzem: ", com)
        time.sleep(2)
        accountBalance -= howMuch
        inf = str(nrOfT) + "; " + str(howMuch) + ": " + com
        # saving transfer history
        historyOfTTemp.append(inf)
        for x in historyOfTTemp:
            historyT = x
        historyOfTTxtS = open("C:/Users/bkwia/Desktop/python/BankProject/data/przelewy.data", "at", encoding="UTF-8")
        if not historyT == []:
            historyOfTTxtS.write(historyT + "\n")
        historyOfTTxtS.close()
        return accountBalance
    else:
        print("Nie ma takiego wyboru")
        time.sleep(2)