c=int(input())
n=int(input())
for i in range(n):
    l,w=map(int,input().split())
    if l<c or w<c:
        print('UPLOAD ANOTHER')
    elif l>=c and w>=c:
        if l==w:
            print('ACCEPTED')
        else:
            print('CROP IT')
