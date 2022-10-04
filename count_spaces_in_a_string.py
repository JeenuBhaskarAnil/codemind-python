st=input()
u=0
l=0
s=0
n=0
sp=0
for i in range(len(st)):
        if st[i].isupper():
            u+= 1
        elif st[i].islower():
            l+= 1
        elif st[i].isdigit():
            n+= 1
        elif st[i]==" ":
            s=s+1
        else:
            sp+=1
print(s)