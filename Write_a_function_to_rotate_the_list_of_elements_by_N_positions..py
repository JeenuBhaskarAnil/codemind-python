n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l=[l[-1]]+l[:n-1]
print(*l)