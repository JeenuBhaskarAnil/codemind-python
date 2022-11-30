l=list(map(int,input().split(",")))
a=[]
for i in l:
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=j
    if f in l:
       a.append(i)
a.sort()
if len(a)==0:
    print("-1")
else:
    for i in a:
        print(i,end=" ")