n=int(input())
l=list(map(int,input().split()))
num=int(input())
c=0
for i in range(n):
    if num==l[i]:
        c=c+1
        print("True")
        break
if c==0:
    print("False")