n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if l.count(i)==1:
        c=c+1
        print(i,"",end="")
if c==0:
    print("-1")
            