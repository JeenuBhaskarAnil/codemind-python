n=input()
l=list(n.split())
s=[]
c=0
for i in range(len(l)):
    k=0
    for j in range(len(l[i])):
        if l[i][j]=='a' or l[i][j]=='u' or l[i][j]=='o' or l[i][j]=='i' or l[i][j]=='e':
              k=k+1
    s.append(k)
b=s.count(min(s))
print(b)
    