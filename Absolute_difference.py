def p(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
        
n=int(input())
l=list(map(int,input().split()))
b=1
a=1
for i in l:
    if p(i):
        b*=i
    else:
        a*=i
print(abs(a-b))
    