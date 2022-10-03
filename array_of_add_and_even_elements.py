n=int(input())
l=list(map(int,input().split()))
li=[]
for i in range(n):
    if l[i]%2!=0:
        li.append(l[i])
for i in range(n):
    if l[i]%2==0:
        li.append(l[i])
for i in range(n):
    print(li[i],"",end="")
        