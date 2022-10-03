n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-1,2):
    for j in range(l[i+1]):
        print(l[i],"",end="")
        