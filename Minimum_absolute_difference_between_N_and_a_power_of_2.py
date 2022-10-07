n=int(input())
l1=[]
for i in range(1,n):
    l1.append(2**i)
for i in l1:
    if i<=n:
        e=i
if n-e<e*2-n:
    print(n-e)
else:
    print(e*2-n)