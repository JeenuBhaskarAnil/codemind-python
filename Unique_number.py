n=int(input())
l=[]
k=0
s=0
while n:
    k=k+1
    l.append(n%10)
    n=n//10
l.sort()
for i in range(k):
    if l[i]-l[i-1]==0:
        s=s+1
        print("Not Unique Number")
        break
if s==0:
    print("Unique Number")
    
    
