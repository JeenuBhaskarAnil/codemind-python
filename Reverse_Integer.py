n=int(input())
k=0
s=0
l=[]
if n<0:
    n=-n
    k=1
while n:
    v=n%10
    if v!=0:
         l.append(v)
    n=n//10
    s=s+1
if k==1:
    print("-",end="")
for i in range(0,s):
    print(l[i],end="")
