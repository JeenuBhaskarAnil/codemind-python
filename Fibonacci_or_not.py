n=int(input())
l=[]
k=0
l.extend({0,1,1})
a=1
b=2
for i in range(n-3):
    l.append(b)
    c=a+b
    a=b
    b=c
for i in range(0,n-1):
    if l[i]==n:
        k=k+1
        break
if k!=0:
    print("True")
else:
    print("False")

