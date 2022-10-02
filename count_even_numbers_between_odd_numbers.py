n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    if l[i]%2==0 and l[i-1]%2!=0 and l[i+1]%2!=0:
        c=c+1
print(c)
    

