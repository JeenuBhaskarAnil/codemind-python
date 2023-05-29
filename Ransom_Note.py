n=(input().split())
r=n[0]
m=n[1]
for i in r:
    if r.count(i)>m.count(i):
        print(1==0)
        break
else:
    print(1>0)
