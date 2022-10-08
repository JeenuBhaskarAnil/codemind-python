n=int(input())
t=0
for i in range(n):
    for j in  range(n):
        if i**2+j**2==n:
            t=t+1
            break
    if t!=0:
        break
if t==0:
    print('False')
else:
    print("True")