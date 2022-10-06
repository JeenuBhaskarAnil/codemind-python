n=int(input())
l=list(map(int,input().split()))
c=[]
k=[]
for i in l:
    if i not in k:
        c.append(l.count(i)//2)
        if l.count(i)//2:
            k.append(i)
print(sum(c))