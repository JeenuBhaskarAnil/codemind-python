n=int(input())
e=0
o=0
m=0
while n:
    d=n%10
    n=n//10
    if d%2==0:
        e=e+1
    else:
        o=o+1
if e==0:
    print('Odd')
elif o==0:
    print('Even')
else:
    print('Mixed')
    
    