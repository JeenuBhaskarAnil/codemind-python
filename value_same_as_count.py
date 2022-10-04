n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i:
       c.append(i)
c=list(dict.fromkeys(c))
print(len(c))