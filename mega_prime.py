n=int(input())
s=0
for i in range(2,n):
    if n%i==0:
        s=s+1
if s==0:
    c=0
    while n:
        d=n%10
        for i in range(2,d):
            if d%i==0:
                c=c+1
        n=n//10
    if d!=1 and c==0:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")