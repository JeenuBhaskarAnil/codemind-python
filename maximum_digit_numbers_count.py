q=int(input())
l=list(map(int,input().split()))
h=[]
for i in l:
    if i<0:
        h.append(len(str(i))-1)
    else:
        h.append(len(str(i)))
m=max(h)
a=[]
for i in l:
  j=i
  if j not in a:
    if i<0:
        i=-i
    if len(str(i))==m :
        a.append(j)
for i in a:
    print(i,end=" ")


    
