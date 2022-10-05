l=input().lower().split()
l=''.join(l)
r=''
for i in range(len(l)-1,-1,-1):
    r=r+l[i]
if l==r:
    print("True")
else:
    print("False")
    