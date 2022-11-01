z=input().split()
l=[]
c=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in z:
    l.append(i)
for n in l:
    for i in range(len(n)//2) :
        if (n[i] in v  and n[-(i+1)] not in v ) or   (n[i] not in v  and n[-(i+1)] in v ):
            c=c+1
print(c)
    