z=int(input())
l=list(map(int,input().split()))
n=int(input())
a=[]
for i in range(len(l)):
    if n==l[i]:
        a.append(i)
if len(a)==0:
    a=[-1,-1]
print(min(a),max(a))