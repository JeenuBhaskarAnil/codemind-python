n=input()
l=list(n.split())
s=[]
for i in range(len(l)):
    s.append(l[i][::-1])
for i in range(len(s)):
    print(s[i],"",end="")

    