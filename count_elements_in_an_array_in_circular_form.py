n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
k.append(l[-1])
for i in range(n):
    k.append(l[i])
k.append(l[0])
for i in range(1,n+1):
    if ((k[i-1] % 2 == 0 and k[i+1] % 2 != 0) or (k[i-1] % 2 != 0 and k[i+1] % 2 == 0)):
        c=c+1
print(c)