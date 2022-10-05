l1=input().lower().split()
l2=input().lower().split()
l1=''.join(l1)
l2=''.join(l2)
g=[]
for i in l2:
    if i in l1:
        g.append(i)
for i in l1:
    if i in l2:
        g.append(i)
c=list(dict.fromkeys(g))
c.sort()
print(len(c))