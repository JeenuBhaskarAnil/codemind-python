n=input()
l=list(n.split())
for i in range(len(l)-1,-1,-1):
    l[i]=l[i][::-1]
    print(l[i],"",end="")