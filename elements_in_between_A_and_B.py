n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i>=a and i<=b:
        c.append(i)
if len(c)==0:
    print("-1")
else:
    for i in c:
       print(i,"",end='')