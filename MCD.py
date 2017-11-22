def MCD(n,m):
    D=max(n,m)
    d=min(n,m)
    r=D%d
    flag=False
    while(r!=0):
        q=int(D/d)
        r=D%d
        D=d
        d=r
        flag=True
    if(flag):
        return D
    else:
        return d

