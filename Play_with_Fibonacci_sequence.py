n=int(input())
l=[0,1,1,2]
a=1
b=2
for i in range(n-4):
    c=a+b
    l.append(c)
    a=b
    b=c
for i in l:
    print(i,"",end='')