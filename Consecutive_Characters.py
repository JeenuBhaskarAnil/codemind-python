n=input()
a=[]
l=[]
for i in range(len(n)):
    c=0
    for j in range(i,len(n)):
        if n[i]==n[j]:
            c=c+1
        else:
            break
    a.append(c)
print(max(a))