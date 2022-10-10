n=input()
a=[]
for i in n:
    a.append(i)
p=[]
l=[]
for i in range(len(n)):
    if n[i] in ('a','e','i','o','u','A','E','I','O','U'):
        l.append(n[i])
        p.append(i)
l.reverse()
r=0
for i in p:
     a[i]=l[r]
     r=r+1
for i in a:
    print(i,end='')