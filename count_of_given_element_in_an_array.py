le=int(input())
l=list(map(int,input().split()))
n=int(input())
c=0
for i in range(0,le):
    if l[i]==n:
        c=c+1
print(c)