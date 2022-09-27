n=int(input())
s=0
p=1
while n:
    s=s+n%10
    p=p*(n%10)
    n=n//10
if s==p:
    print("Spy Number")
else:
     print("Not Spy Number")