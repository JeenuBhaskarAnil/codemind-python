m,n=map(int,input().split())
l=list(map(int,input().split()))
l=l[n:len(l)]+l[0:n]
for i in l:
    print(i,end=" ")