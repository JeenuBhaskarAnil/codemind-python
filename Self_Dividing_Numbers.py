n=int(input())
m=int(input())
for i in range(n,m+1):
    h=i
    u=0
    if i%10!=0:
        s=0
        while i:
            k=i%10
            i=i//10
            if h%k!=0:
                s=s+1
        if s==0:
            print(h,"",end="")
            





        