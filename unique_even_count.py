n=int(input())
l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
c=0
for i in l:
    if l.count(i)==1 and i%2==0:
        c=c+1
print(c)