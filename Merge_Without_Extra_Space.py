for i in range(int(input())):
    m,n=map(int,input().split())
    lll=list(map(int,input().split()))
    ll=list(map(int,input().split()))
    l=ll+lll
    l.sort()
    print(*l)
    