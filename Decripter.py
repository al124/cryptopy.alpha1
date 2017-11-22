import Converter
import os
def decrypt():
    ltesti=os.listdir() #lista file nella cartella corrente
    if ("cmessage.txt" not in ltesti):
        return None
    else:
        with open("cmessage.txt","r",encoding="utf-8")as f:
            message=f.read()
        numeric10 = Converter.fromStr_to10(message)
        with open("keys.txt")as f:
            pkeys = f.read().split()
        with open("pr_keys.txt")as f:
            h = int(f.read())
        N=int(pkeys[0])
        new_numeric10=pow(numeric10,h,N)
        new_message=Converter.from10_toStr(new_numeric10)
        with open("clear_message.txt","w",encoding="utf-8")as f:
            f.write(new_message)
decrypt()