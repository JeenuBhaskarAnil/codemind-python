l1=input().lower().split()
l1=''.join(l1)
l2=input().lower().split()
l2=''.join(l2)
c=0
for i in l1:
    if i in l2:
        c=c+1
    
if c==len(l1):
        print("True")
else:
        print("False")