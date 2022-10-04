n=input()
c=0
l=[]
f=[]
v=['a','e','i','o','u']
for i in range(len(n)):
    l.append(n[i])
l=list(dict.fromkeys(l))
uc=list(set(v)^set(l))
for i in range(len(uc)):
    if uc[i]=='a' or uc[i]=='e' or uc[i]=='o' or uc[i]=='i' or uc[i]=='u':
        c=c+1
        f.append(uc[i])
if c==0:
    print("0")
else:
    f.sort()
    for i in range(len(f)):
        print(f[i],'',end='')
