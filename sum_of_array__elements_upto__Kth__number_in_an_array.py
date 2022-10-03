n=int(input())
l=list(map(int,input().split()))
k=int(input())
s1=0
for i in range(0,n):
    if i==k:
        break
    s1=s1+l[i]
print(s1)