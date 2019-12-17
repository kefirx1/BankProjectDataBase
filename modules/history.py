import os

def history(historyOfT, ):
    counter = 1
    os.system("cls")
    for trans in historyOfT:
        pAddress = trans.index(";")
        pAmount = trans.index(":")
        pComment = trans.index("\n")
        address = trans[0:pAddress]
        amount = trans[pAddress + 2: pAmount]
        comment = trans[pAmount + 2: pComment]
        print("--------------------------------")
        print("Przelew nr ", counter)
        print("Adres: ", address)
        print("Kwota: ", amount)
        print("Komentarz: ", comment)
        print("--------------------------------")
        counter += 1
    input()