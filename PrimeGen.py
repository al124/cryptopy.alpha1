import random
import primality
def PrimeGet():
    with open("primes.txt")as f:
        primi=f.read()
    primi=primi.split(" ")
    retry=True
    retry1=False
    while(retry):
        try:
            primo=int(random.choice(primi))
        except ValueError:
            retry1=True
        if(retry1==False):
            retry=False
    return(primo)
def randomPrime():
    c=True
    while(c):
        #Numero con 100-138 cifre
        n=random.randint(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        if(primality.miller_rabin(n,200)):
            c=False
    return n
