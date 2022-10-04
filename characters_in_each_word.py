n=input()
l=list(n.split())
s=[]
for i in range(len(l)):
    s.append(len(l[i]))
for i in range(len(s)):
    print(s[i],"",end="")