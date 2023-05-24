n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
if len(a)<3:
    print(max(l))
else:
    print(a[2])