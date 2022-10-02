n=int(input())
f=0
s=0
for i in range(2,n):
    if n%i==0:
        f=f+1
if n!=0 and f==0:
    s=s+1
r=0
fa=0
sr=0
while n:
    r=r*10+n%10
    n=n//10
for i in range(2,r):
    if r%i==0:
        fa=fa+1
if r!=0 and fa==0:
    sr=sr+1
if s==0:
    print("not prime")
elif s!=0 and sr!=0:
    print("circular prime")
else:
    print("prime but not a circular prime")
    