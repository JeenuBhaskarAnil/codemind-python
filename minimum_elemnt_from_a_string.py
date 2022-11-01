z=input().split()
n=z[-1]
l=[]
for i in n:
    l.append(i)
m=min(l)
if m.lower() in n:
    print(m.lower())
else:
    print(m)
    