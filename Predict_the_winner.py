n=int(input())
l=list(map(int,input().split()))
lx=0
ly=0
for i in range(0,len(l)-1,2):
    lx=lx+l[i]
    ly=ly+l[i+1]
if (lx-ly)%4==0:
    print("X")
else:
    print("Y")
