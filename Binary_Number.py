z=int(input())
for i in range(2**z):
    n=i
    b=0
    p=0
    d=0
    while n:
        b=b+(n%2)*10**p
        n=n//2
        p=p+1
        d=d+1
    if p==z:
        print(b)
    else:
        l=[]
        for i in range(z-d):
            l.append(0)
        l.append(b)
        if len(l)>z:
            l.pop()
        for g in l:
            print(g,end='')
        print()
    