n=int(input())
l=list(map(int,input().split()))
s1=0
for i in range(n):
    if l[i]%2==0:
        s1=s1+l[i]
print(s1)