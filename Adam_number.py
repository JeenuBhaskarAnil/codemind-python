n=int(input())
n2=n*n
s=0
while n:
    s=s*10+n%10
    n=n//10
m2=s**2
k=0
while m2:
 k=k*10+m2%10
 m2=m2//10
if k==n2:
    print("True")
else:
    print("False")