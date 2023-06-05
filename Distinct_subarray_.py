from itertools import combinations
n=int(input())
m=int(input())
l=[i for i in range(n,m+1)]
a=[]
for i in range(1,3):
     m=list(combinations(l,i))
     a+=m
c=0
#print(a)
for i in a:
    if sum(i)%2!=0:
        c+=1
print(c)