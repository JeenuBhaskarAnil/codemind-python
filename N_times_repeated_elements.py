n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
for i in l:
    if l.count(i)==k:
       c.append(i)
c=list(dict.fromkeys(c))
if len(c)!=0:
 for i in c:
    print(i,"",end="")
if len(c)==0:
    print("-1")