n=int(input())
l=list(map(int,input().split()))
m=min(l)
c=0
k=0
while m:
    c=c+1
    m=m//10
for i in l:
    d=0
    while i:
        d=d+1
        i=i//10
    if d==c:
        k=k+1
print(k)