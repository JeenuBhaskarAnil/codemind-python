n=int(input())
for i in range(n):
    m=input()
    c=0
    for i in m:
        if i not in ('1','0','2','3','4','5','6','7','8','9'):
            c=c+1
    if c==0:
        print("True")
    else:
        print("False")