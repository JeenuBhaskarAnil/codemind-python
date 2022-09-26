def add(x):
    sum=0
    while x>0:
        sum=sum+x%10
        x=x//10
    return sum
t=int(input())
while t>0:
    t=add(t)
    r=t
    if r<10:
        break
print(r)


    