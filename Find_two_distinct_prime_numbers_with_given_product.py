n=int(input())
t=0
for i in range(2,n):
    if n%i==0:
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if c==0:
            g=i
            q=n//i
            d=0
            for k in range(2,q):
                if q%k==0:
                    d=d+1
                if d==0:
                    t=t+1
                    break
if t!=0:
    print(q,g)
else:
    print("-1")