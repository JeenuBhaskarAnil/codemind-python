n=int(input())
while n:
    s=0
    while n:
        s=s+(n%10)**2
        n=n//10
    n=s
    if n<10:
        break
if n==1 or n==7:
    print("True")
else:
    print("False")
    
    
