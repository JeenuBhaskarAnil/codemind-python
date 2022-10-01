n=int(input())
m=n
v=n
s=0
while n:
    s=s+1
    n=n//10
k=0
while m:
    d=m%10
    k=k+d**s
    s=s-1
    m=m//10
if k==v:
    print("True")
else:
    print("False")

     