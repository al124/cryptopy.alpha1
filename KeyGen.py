import bezout
import MCD
import random
import PrimeGen


class KeyGen:
    def __init__(self):
        self.p=PrimeGen.randomPrime()
        self.q=PrimeGen.randomPrime()
        self._keys()
    def _keys(self):
        self.N=self.p*self.q
        self.Phi=(self.p-1)*(self.q-1)
        NotGen=True
        while(NotGen):
            d=random.randint(1,self.Phi-1)
            mcd=MCD.MCD(d,self.Phi)
            if mcd==1:
                self.d=d
                NotGen=False
        self.h=bezout.Bresult(self.d,self.Phi)
        if(self.h<0):
            self.h=self.h+self.Phi
        return None
    def Public_Key(self):
        return self.N,self.d
    def Private_Key(self):
        return self.Phi,self.h


test=KeyGen()
N,d=test.Public_Key()
P,h=test.Private_Key()
testo=str(N)+"  "+str(d)
testo1=str(h)
with open("keys.txt",'w')as f:
    f.write(testo)
with open("pr_keys.txt",'w')as f:
    f.write(testo1)

'''m=592
print(N)
print(d)
print(h)
mc=pow(m,d,N)
dcm=pow(mc,h,N)
print(dcm)'''


