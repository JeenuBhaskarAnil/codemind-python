n=int(input())
m=int(input())
for i in range(n+1,m):
    s=0
    for j in range(2,i):
        if i%j==0:
            s=s+1
    if s==0:
     print(i)