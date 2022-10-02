n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(n):
    if l[i]%2==0:
        s1=s1+l[i]
    else:
        s2=s2+l[i]
if s2>s1 :
    print(s2-s1) 
else: 
    print(s1-s2)
