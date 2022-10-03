n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    c=0
    while l[i]:
        c=c*10+l[i]%10
        l[i]=l[i]//10
    s.append(c)
for i in range(n):
    print(s[i],"",end="")
