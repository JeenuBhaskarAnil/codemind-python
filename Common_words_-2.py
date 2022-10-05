l1=list(input().lower().split())
l2=list(input().lower().split())
c=0
d=[]
for i in l2:
    if l2.count(i)!=2 and l1.count(i)!=2:
        if i in l1:
            c=c+1
print(c)