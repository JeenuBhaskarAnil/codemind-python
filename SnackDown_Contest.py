for i in range(int(input())):
    n=int(input())
    l=[i for i in range(1,n+1)]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k=a+b
    for i in l:
        if i not in k:
            print("NO")
            break
    else:
        print("YES")