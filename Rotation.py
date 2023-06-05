for i in range(int(input())):
    m,n=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(n):
        l=[l[-1]]+l[:m-1]
    print(*l)