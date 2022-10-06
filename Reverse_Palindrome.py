n=int(input())
while n:
    r=0
    h=n
    while n:
        r=r*10+n%10
        n=n//10
    f=h+r
    j=f
    rf=0
    while f:
        rf=rf*10+f%10
        f=f//10
    if rf==j:
        print(rf)
        break
    else:
        n=j