def f(n):
    m=n
    while n:
        r=n%10
        if r==0:
            return False
        else:
            if m%r!=0:
                return False
        n=n//10
    return True
for i in range(int(input()),int(input())+1):
    if f(i):
        print(i,end=" ")