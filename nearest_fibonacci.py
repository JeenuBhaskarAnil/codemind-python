l=[0,1,2,3,5,8,13]
for i in range(10):
    l.append(l[-1]+l[-2])
n=int(input())
a=[]
for i in range(len(l)-1):
    if n>=l[i] and n<l[i+1]:
        a.append(l[i])
        a.append(l[i+1])
if n-a[0]<a[1]-n:
    print(a[0])
elif n-a[0]==a[1]-n:
    print(a[0],a[1])
else:
    print(a[1])
