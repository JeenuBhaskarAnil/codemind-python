z=int(input())
l=list(map(int,input().split()))
n=int(input())
l1=l[0:len(l)//2]
l2=l[len(l)//2:len(l)]
a=[]
for i in range(len(l)//2):
    a.append(l1[i])
    a.append(l2[i])
for i in a:
    print(i,end=" ")
