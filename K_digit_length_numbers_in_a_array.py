n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(n):
    c=0
    if l[i]<0:
        l[i]=-l[i]
    if l[i]==0:
        l[i]=1
    while l[i]:
        c=c+1
        l[i]=l[i]//10
    if c==k:
        s=s+1
print(s)
