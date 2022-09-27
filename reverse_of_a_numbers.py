n=int(input())
k=0
l=[]
while n:
    l.append(n%10)
    n=n//10
    k=k+1
for i in range(k):
    print(l[i],end="")