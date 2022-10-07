z=int(input())
for x in range(z):
    n=input()
    c=0
    for i in n:
        if i in ('0','1','2','3','4','5','6','7','8','9'):
            c=c+1
    if c==0:
        print('No')
    else:
        print('Yes')