n=int(input())
c=0
for i in range(1,n+1):
 if n%i==0:   
  s=0
  for j in range(2,i):
    if i%j==0:
        s=s+1
  if s!=0:
      c=c+1
print(c+1)
      
        
    