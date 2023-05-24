n=int(input())
l=list(map(int,input().split()))
m=int(input())
a=list(map(int,input().split()))
for i in a:
    if i not in l:
        print("False")
        break
else:
    print("True")