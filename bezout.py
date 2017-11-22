def bezoutcoef(b, n):
    tempb=max(b,n)
    tempn=min(b,n)
    b=tempb
    n=tempn
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0,y0
def Bresult(b,n):
    x,y=bezoutcoef(b,n)
    mod=n
    cong=(b*y)%mod
    if(cong==1):
        return y
    else:
        return x

