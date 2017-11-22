def to_byte(text):
    btext=""
    for c in text:
        b=str(bin(ord(c)))[2:]
        while(len(b)<8):
            b="0"+b
        btext+=b
    return btext

def to_ascii(btext):
    text=""
    i=0
    for counter in range(int((len(btext))/8)):
        bc=btext[i:(8*(counter+1))]
        c=chr(int(bc,2))
        i=i+8
        text=text+c
    return text
def to_base10(binNum):
    return (int(binNum,2))
def to_base2(decNum):
    b2=bin(decNum)[2:]
    while(len(b2)%8!=0):
        b2="0"+b2
    return b2
def fromStr_to10(text):
    bin=to_byte(text)
    dec=to_base10(bin)
    return dec
def from10_toStr(dec):
    bin=to_base2(dec)
    mess=to_ascii(bin)
    return mess
