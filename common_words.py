n=input().lower().split()
m=input().lower().split()
a=[]
for i in m:
    if i in n:
        a.append(i)
print(*a)