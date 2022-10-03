n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    while l[i]:
        c=c+l[i]%10
        l[i]=l[i]//10
print(c)
