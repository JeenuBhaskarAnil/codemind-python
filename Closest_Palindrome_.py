n=int(input())
for i in range(n-1,10,-1):
    s=0
    m=i
    while i:
        s=s*10+(i%10)
        i=i//10
    if m==s:
        f=s
        break
for i in range(n+1,2*n):
    s=0
    m=i
    while i:
        s=s*10+(i%10)
        i=i//10
    if m==s:
        g=s
        break
if n-f>g-n:
    print(g)
elif n-f<g-n:
    print(f)
else:
    print(f,g)
    
       