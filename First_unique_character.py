l=input().lower().split()
s=''.join(l)
c=0
for i in s:
    if s.count(i)==1:
        print(i)
        c=c+1
        break
if c==0:
    print("-1")