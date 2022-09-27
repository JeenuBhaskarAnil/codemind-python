n=int(input())
k=0
l=[]
while n:
    l.append(n%10)
    n=n//10
    k=k+1
l.sort()
print(l[k-1])

