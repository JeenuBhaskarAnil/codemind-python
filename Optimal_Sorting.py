n=int(input())
for i in range(n):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            c=c+1
    if c==0:
        print("0")
    else:
        print(max(l)-min(l))
        