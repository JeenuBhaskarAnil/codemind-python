n=int(input())
li=list(map(int,input().split()))
l=[]
c=0
l.append(li[len(li)-1])
for i in range(n):
    l.append(li[i])
l.append(li[0])
for i in range(1,n+1):
    if (l[i-1]%2!=0 and l[i+1]%2==0) or (l[i-1]%2==0 and l[i+1]%2!=0):
        c=c+1
print(c)






