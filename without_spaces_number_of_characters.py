n=input()
l=list(n.split())
s=0
for i in range(len(l)):
    s=s+len(l[i])
print(s)