def f(n):
    for i in range(2,n):
        if n%i==0:
            return 0>1
    return 1>0
   
n=int(input())
b=[]
for i in range(2,n):
    if f(i):
        b.append(i)
for i in range(n+1,n**3):
    if f(i):
        b.append(i)
        break
l=b[-2]
r=b[-1]
ld=abs(l-n)
rd=abs(r-n)
if f(n):
    print("0")
elif ld>=rd:
    print(rd)
else:
    print(ld)
