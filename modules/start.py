import time, os, sys

def welcome():
    print("-------------\nWitamy w BBP\n-------------")
    time.sleep(2)
    os.system("cls")


def authentication():
    for i in range(4):
        j = 3 - i
        pin = input("Wprowadz PIN: ")
        if j == 0:
            print("Blokowanie konta")
            time.sleep(2)
            sys.exit()
        if pin == "1234":
            print("Logowanie...")
            time.sleep(2)
            os.system("cls")
            return True
        else:
            print("Zly pin")
            time.sleep(1)
            os.system("cls")
            print("Pozostalo ", j, " prob")