m,n=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
s=0
for i in l:
    if i==sorted(i) or i==sorted(i,reverse=True):
        s+=1
print(s)