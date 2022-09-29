n=int(input())
k=0
l=[]
if n<=0:
    print("Not Ugly Number")
else:
    for i in range(2,n+1):
        if n%i==0 and i!=2 and i!=3 and i!=5:
            l.append(i)
            k=k+1
    g=0        
    for m in l:
        f=0
        for j in range(2,m):
            if m%j==0:
                f=f+1
        if f==0:
            g=g+1
    if g==0:
        print("Ugly Number")
    else:
        print("Not Ugly Number")

