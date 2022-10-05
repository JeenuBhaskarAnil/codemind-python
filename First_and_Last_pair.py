n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)//2):
    r.append(l[i])
    r.append(l[len(l)-(i+1)])
if len(l)%2!=0:
    r.append(l[len(l)//2])
    r.append(0)
for i in r:
    print(i,'',end='')