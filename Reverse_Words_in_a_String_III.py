l=input().split()
for i in l:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end='')
    print(' ',end='')