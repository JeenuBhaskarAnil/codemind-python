n=input().split()
v='aeiouAEIOU'
a="a"
p=1
for l in n:
    r=''
    if l[0] in v:
        r=r+l+"ma"+a*p
    else:
        r=r+l[1:]+l[0]+"ma"+a*p
    p+=1
    print(r,end=" ")