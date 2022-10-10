for z in range(int(input())):
    l=int(input())
    n=input()
    c=0
    for i in n:
        if n.count(i)==1:
            print(i)
            c=c+1
            break
    if c==0:
        print('-1')