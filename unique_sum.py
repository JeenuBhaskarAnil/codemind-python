n=int(input())
l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
c=[]
for i in l:
    if l.count(i)==1:
        c.append(i)
print(sum(c))