n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n//2):
    s1=s1+l[i]
for i in range(n//2,n):
    s2=s2+l[i]
print(s2-s1)
    