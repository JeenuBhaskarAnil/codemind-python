n=input()
c=0
l=[]
for i in range(len(n)):
    l.append(n[i])
for i in range(len(l)):
    if l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u'or l[i]=='A' or l[i]=='E' or l[i]=='I' or l[i]=='O' or l[i]=='U':
        c=c+1
print(c)
