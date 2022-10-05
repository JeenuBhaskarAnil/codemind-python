l=input().lower().split()
c=0
for i in l:
    r=''
    for j in range(len(i)-1,-1,-1):
        r=r+i[j]
    if r==i:
        c=c+1
print(c)
