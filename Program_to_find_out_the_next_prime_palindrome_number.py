n=int(input())
for i in range(n+1,n*100):
    rev=0
    f=0
    m=i
    while i:
        d=i%10
        rev=rev*10+d
        i=i//10
    if rev==m:
        for j in range(2,m):
            if m%j==0:
                f=f+1
        if f==0:
            print(m)
            break
    