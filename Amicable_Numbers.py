n=int(input())
m=int(input())
sn=0
sm=0
for i in range(1,n):
    if n%i==0:
        sn=sn+i
for i in range(1,m):
    if m%i==0:
      sm=sm+i
if sm==n and sn==m:
    print("Amicable")
else:
    print("Not Amicable")
