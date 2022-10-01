z=int(input())
for i in range(z):
    n=int(input())
    for i in range(n,1,-1):
            c=0
            for j in range(2,i):
                if i%j==0:
                    c=c+1
            if i!=1 and c==0:
                f=i
                break
    for i in range(n,n*n):
            c=0
            for j in range(2,i):
                if i%j==0:
                    c=c+1
            if i!=1 and c==0:
                g=i
                break
    if n-f<=g-n:
        print(f)
    else :
        print(g)
        
      
    