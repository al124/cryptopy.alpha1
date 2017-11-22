import Converter
import os
def encrypt():
    ltesti=os.listdir() #lista file nella cartella corrente
    if ("message.txt" not in ltesti):
        return None
    else:
        with open("message.txt","r")as f:
            message=f.read()
        numeric10 = Converter.fromStr_to10(message)
        with open("keys.txt")as f:
            pkeys = f.read().split()
        N=int(pkeys[0])
        d=int(pkeys[1])
        new_numeric10=pow(numeric10,d,N)
        new_message=Converter.from10_toStr(new_numeric10)
        with open("cmessage.txt","w",encoding="utf-8")as f:
            f.write(new_message)
encrypt()
