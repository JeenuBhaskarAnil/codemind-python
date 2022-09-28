n=int(input())
m=n
s=0
while n>0:
    s=s*10+n%10
    n=n//10
if m!=s:
    print("False")
else:
    print("True")