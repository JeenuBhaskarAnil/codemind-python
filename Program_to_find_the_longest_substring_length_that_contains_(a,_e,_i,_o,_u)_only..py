n=input()
l=[]
for i in n:
    l.append(i)
a=[]
for i in range(len(l)):
    c=0
    for j in range(i,len(l)):
        if l[i] in ('a','e','i','o','u') and l[j] in ('a','e','i','o','u'):
            c=c+1
        else:
            break
    a.append(c)
print(max(a))
    