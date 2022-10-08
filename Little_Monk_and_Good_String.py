n=input()
l=[]
for i in range(len(n)):
    c=0
    for j in range(i,len(n)-1):
        if n[j] in ('a','e','i','o','u') and n[j+1] in ('a','e','i','o','u'):
            c=c+1
        else:
            break
    l.append(c)
print(max(l)+1)