for i in range(int(input())):
    n=input()
    c=0
    for i in range(0,len(n)-1):
     if n[i]==n[i+1]:
        c=c+1
    print(c)