n,r,t=map(int,input().split())
l=list(map(int,input().split()))
for i in range(r):
    l=[l[-1]]+l[:n-1]
for i in range(t):
    print(l[int(input())])