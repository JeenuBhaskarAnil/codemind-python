n,r=map(int,input().split())
for i in range(1,r+1):
    if i%2!=0:
        print("{} x {} = {}".format(n,i,n*i))