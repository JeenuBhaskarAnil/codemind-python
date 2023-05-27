l=input().lower().split()
li=[]
r=''
for i in l:
    li.append(set(i))
a=li[0]
for i in range(1, len(li)):
    a=a.intersection(li[i])
if len(a)!=0:
    print(min(a))
else:
    print("-1")
    


