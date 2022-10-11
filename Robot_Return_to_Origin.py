n=input()
l=[]
for i in n:
    l.append(i)
c=0
for i in l:
    if i=="U" :
        c=c+1
    if i=='D':
        c=c-1
    if i=='R':
        c=c+2
    if i=='L':
        c=c-2
if c==0:
    print('True')
else:
    print('False')
    