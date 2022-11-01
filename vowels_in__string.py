n=input()
l=[]
for i in n:
    if i in ('a','e','i','o','u','A','E','I','O','U') and i not in l:
        l.append(i)
if len(l)==0:
    print('-1')
else:
    for i in l:
        print(i,end=' ')
    

