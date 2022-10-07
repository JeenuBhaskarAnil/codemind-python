z=int(input())
for x in range(z):
    n=int(input())
    m=n
    s=0
    while n:
        s=s*10+n%10
        n=n//10
    if m!=s:
        print("False")
    else:
        print("True")