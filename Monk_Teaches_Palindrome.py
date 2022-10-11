for z in range(int(input())):
    n=input()
    r=''
    for i in range(len(n)-1,-1,-1):
        r=r+n[i]
    if r!=n:
        print('NO')
    else:
        if len(r)%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')