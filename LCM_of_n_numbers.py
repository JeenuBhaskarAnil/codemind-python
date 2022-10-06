n=int(input())
l=list(map(int,input().split()))
cm=[]
lcm=[]
for i in l:
    for j in range(1,1000):
        cm.append(i*j)
for i in cm:
    if cm.count(i)==n:
        lcm.append(i)
print(min(lcm))