from math import sqrt
def p(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
c=0
for i in range(int(input()),int(input())+1):
    if p(i) and i!=1:
        c+=1
print(c)