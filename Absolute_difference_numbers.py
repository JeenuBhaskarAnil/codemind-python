m,n=map(int,input().split())
l=[]
z=n
a=0
b=0
while m:
    d=m%10
    l.append(d)
    m=m//10
i=0
while i<z:
    a=a+l[i]*10**i
    i=i+1
i=0
h=len(l)-1
while i<z:
    b=b*10+l[h]
    h-=1
    i=i+1
if a>=b:
    print(a-b)
else:
    print(b-a)

    
    
    