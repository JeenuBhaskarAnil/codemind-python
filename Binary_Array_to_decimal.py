n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+l[i]*2**(n-i-1)
print(s)
