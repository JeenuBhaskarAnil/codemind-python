z=int(input())
l=list(map(int,input().split()))
n=int(input())
for i in range(len(l)):
     if l[i]==n:
         print(i)
         break
else:
    print("-1")