n=int(input())
l=list(map(int,input().split()))
f=l[0:len(l):2]
v=l[1:len(l):2]
s=''
for i in range(len(f)):
    s=s+f[i]*str(v[i])
for i in s:
    print(i,end=" ")