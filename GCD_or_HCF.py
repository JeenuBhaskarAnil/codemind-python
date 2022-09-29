n,m=map(int,input().split())
ln=[]
lm=[]
k=0
for i in range(1,100):
    ln.append(i*n)
    lm.append(i*m)
    k=k+1
for i in range(k):
    t=0
    for j in range(k):
        if ln[j]==lm[i]:
          z=ln[j]
          t=t+1
          break
    if t!=0:
        break
print((n*m)//z)
