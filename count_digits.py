n=int(input())
l=list(map(int,input().split()))
s=[]

for i in range(n):
    c=0
    if l[i]<0:
        l[i]=-l[i]
    if l[i]==0:
        l[i]=1
    while l[i]:
        c=c+1
        l[i]=l[i]//10
    s.append(c)
for i in range(n):
    print(s[i],"",end="")
