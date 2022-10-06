n=int(input())
z=n
s=0
while n:
    d=n%10
    n=n//10
    f=1
    if d!=0:
     while d:
        f=f*d
        d=d-1
    s=s+f
if s==z:
    print("The number {} is a strong number".format(z))
else:
    print("The number {} is not a strong number".format(z))
        
        