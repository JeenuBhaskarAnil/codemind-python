a=int(input())
b=int(input())
l=[]
for i in range(a,b):
    j=i
    r=0
    while i:
        r=r*10+i%10
        i=i//10
    if r==j:
        l.append(j)
for i in l:
    print(i,'',end='')