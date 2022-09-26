n=int(input())
l=[]
c=0
while n:
    d=n%10
    n=n//10
    c=c+1
    l.append(d)
l.reverse()
f=0
for i in range(c):
    if l[i]==6:
        l[i]=9
        f=f+1
    if f!=0:
        break
for i in range(c):
    print(l[i],end="")


    
    
    