n=int(input())
s=0
p=1
while n:
    p=p*(n%10)
    s=s+n%10
    n=n//10
print(p-s)
    