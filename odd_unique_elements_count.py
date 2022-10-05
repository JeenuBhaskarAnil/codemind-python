n=int(input())
l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
c=0
for i in l:
    if i<0:
        i=-i
    if i%2!=0 and l.count(i)==1:
        c=c+1
print(c) 