n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
r=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

if len(o)>=len(e):
    for i in range(len(e)):
        r.append(e[i])
        r.append(o[i])
    for i in range(len(e),len(o)):
        r.append(o[i])
if len(e)>len(o):
    for i in range(len(o)):
        r.append(e[i])
        r.append(o[i])
    for i in range(len(o),len(e)):
        r.append(e[i])
if len(r)%2!=0:
    r.append('0')
for i in r:
    print(i,end=" ")
    