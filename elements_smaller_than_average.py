n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
c=0
for i in range(n):
    if l[i]<=a:
        c=c+1
print(c)