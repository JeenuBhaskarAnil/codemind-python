n=input()
c=0
l=[]
v=['a','e','i','o','u']
for i in range(len(n)):
    l.append(n[i])
l=list(dict.fromkeys(l))
for i in range(len(v)):
    for j in range(len(l)):
     if v[i]==l[j]:
        c=c+1
        
if c==5:
    print("True")
else:
    print("False")
