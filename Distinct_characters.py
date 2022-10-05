l=input().lower().split()
s=''.join(l)
c=[]
for i in s:
    if s.count(i)==1:
        c.append(i)
c.sort()
for i in c:
    print(i,end="")
        