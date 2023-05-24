n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)-1):
    s=l[i+1]
    for j in range(i+1,len(l)):
        if s<l[j]:
            s=l[j]
    a.append(s)
a.append(-1)
for i in a:
    print(i,end=" ")
    