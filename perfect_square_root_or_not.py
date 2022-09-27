n=int(input())
k=0
for i in range(1,n):
    if n%i==0:
        if i*i==n:
            k=k+1
            print("True")
            break
if k==0:
    print("False")
