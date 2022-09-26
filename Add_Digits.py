n=int(input())
while n:
    sum=0
    while n:
        sum=sum+n%10
        n=n//10
    n=sum
    if n<10:
        break
print(n)
