n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            p.append(l[j]-l[i])
if len(p)==0:
    print("0")
else:
    print(max(p))