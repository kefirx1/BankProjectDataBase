import os, time, sys
import pymysql as p


def transfer(number):
    date = date=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

    #Connect with data base
    try:
        myBaseT = p.connect(host="localhost", user="root", db="bank")
    except:
        print("Nie udało połączyć się z bazą danych")
        time.sleep(2)
        sys.exit()
    cursor = myBaseT.cursor()

    #checking balance
    cursor.execute("SELECT balance FROM data WHERE number={}".format(number))
    accountBalanceB = cursor.fetchall()
    print(accountBalanceB)
    for ch in accountBalanceB:
        for v in ch:
            accountBalance=v

    os.system("cls")
    print("Stan konta: ", accountBalance, "zl")
    nrOfT = input("Numer konta odbiorcy: ")
    while(True):
        try:
            howMuch = float(input("Podaj kwote przelewu: "))
        except:
            print("Podaj właściwą kwotę")
            continue
        else:
            break


    com = input("Komentarz do przelewu: ")
    back = input("Anuluj(tak/nie): ")
    if back == "tak":
        os.system("cls")
        print("Anulowanie... ")
        time.sleep(2)
        cursor.close()
        myBaseT.close()
        return 
    elif back == "nie":
        if howMuch > accountBalance:
            print("Kwota przelewu: ", howMuch, "jest wieksza niz stan konta: ", accountBalance)
            time.sleep(2)
            cursor.close()
            myBaseT.close()
            return 
        print("Wysylanie przelewu pod numer: ", nrOfT, ", o kwocie: ", howMuch, " zl", " , z komentarzem: ", com)
        time.sleep(2)
        #change balance
        accountBalance -= howMuch
        cursor.execute("UPDATE data SET balance = {} WHERE number={}".format(accountBalance, number))
        myBaseT.commit()
        #saving history
        cursor.execute("INSERT INTO `{}`(date, accountNumber, amount, comment) VALUES ('{}' , '{}' , {} , '{}')".format(number, date, nrOfT, howMuch, com))
        myBaseT.commit()
        cursor.close()
        myBaseT.close()
        return 
    else:
        print("Nie ma takiego wyboru")
        time.sleep(2)
        cursor.close()
        myBaseT.close()
    cursor.close()
    myBaseT.close()
