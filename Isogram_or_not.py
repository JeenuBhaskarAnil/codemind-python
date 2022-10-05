l=input().split()
l=''.join(l)
c=0
for i in l:
    if l.count(i)==1:
        c=c+1
if c==len(l):
    print("True")
else:
    print("False")
        