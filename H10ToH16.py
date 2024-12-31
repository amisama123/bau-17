def H10ToH16(n):
    if n>0:
        sd=n%16
        n=n//16
        if sd==10:
            sd='A'
        if sd==11:
            sd='B'
        if sd ==12:
            sd='C'
        if sd ==13:
            sd='D'
        if sd ==14:
            sd='E'
        if sd ==15:
            sd='F'
        H10ToH16(n)
        print(sd,end='')
n=317547
print(H10ToH16(n))