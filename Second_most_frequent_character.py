l=[]
h=[]
c=0
n=input()
for i in range(len(n)):
    l.append(n[i])
    l.append(n.count(n[i]))
    h.append(n.count(n[i]))
for i in range(1,len(n)):
    if n[i]!=n[i-1]:
        c=c+1
if c!=0 and max(h)!=min(h):
 h.sort()
 for i in range(len(h)-1,-1,-1):
     if h[i]<max(h):
         m=h[i]
         break
 for i in range(1,len(l)):
    if m==l[i]:
        print(l[i-1])
        break
else:
    print('-1')
        