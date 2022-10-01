k=int(input())
m=int(input())
r=m+k
for i in range(1,100):
   n=r+i
   c=0
   for j in range(2,n):
       if n%j==0:
           c=c+1
   if c==0:
        print(i)
        break