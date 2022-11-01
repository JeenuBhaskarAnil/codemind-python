n=input()
c=0
v=['a','e','i','o','u','A','E','I','O','U']
k=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in range(len(n)//2) :
        if (n[i] in v  and n[-(i+1)].lower() in k ) or   (n[i].lower() in k  and n[-(i+1)] in v ):
            c=c+1
print(c)
    