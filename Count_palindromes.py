n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    r=l[i]
    c=0
    while l[i]:
        c=c*10+l[i]%10
        l[i]=l[i]//10
    if r==c:
        s=s+1
print(s)

