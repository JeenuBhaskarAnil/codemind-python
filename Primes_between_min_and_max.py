n=int(input())
l=list(map(int,input().split()))
s1=0
a=l.index(min(l))
b=l.index(max(l))
if a>b:
    a,b=b,a
for i in range(a,b+1):
    f=0
    for j in range(2,l[i]):
        if l[i]%j==0:
            f=f+1
    if l[i]>1 and f==0:
        s1=s1+1
print(s1)