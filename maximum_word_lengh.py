n=input()
l=list(n.split())
s=[]
for i in range(len(l)):
    s.append(len(l[i]))
print(max(s))