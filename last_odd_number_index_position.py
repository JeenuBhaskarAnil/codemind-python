le=int(input())
l=list(map(int,input().split()))
for i in range(le-1,-1,-1):
    if l[i]%2!=0:
        print(i)
        break
          