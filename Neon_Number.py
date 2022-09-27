n=int(input())
m=n*n
s=0
while m:
    s=s+m%10
    m=m//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    