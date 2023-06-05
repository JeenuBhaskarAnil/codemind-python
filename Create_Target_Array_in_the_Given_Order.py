n=int(input())
l=list(map(int,input().split()))
m=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    r.insert(a[i],l[i])
print(*r)