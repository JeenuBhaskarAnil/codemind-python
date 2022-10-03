n=int(input())
l=list(map(int,input().split()))
k=int(input())
s1=0
for i in range(0,n):
    f=0
    for j in range(2,l[i]):
        if l[i]%j==0:
            f=f+1
    if l[i]<=k and l[i]>1 and f==0:
        s1=s1+1
print(s1)