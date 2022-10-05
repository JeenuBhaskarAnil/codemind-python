l1=list(input().lower().split())
l2=list(input().lower().split())
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)
