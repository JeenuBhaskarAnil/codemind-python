n=input()
n=n[::-1]
i=0
l=[]
while i!=len(n):
    if n[i]=='#':
        l.append(n[i:i+3])
        i=i+3
    else:
        l.append(n[i])
        i+=1
l=l[::-1]
a=[]
for i in l:
    a.append(i[::-1])
l=[]
for i in range(1,10):
    l.append(str(i))
    l.append(chr(i+96))
for i in range(10,27):
    l.append(str(i)+"#")
    l.append(chr(i+96))
s=''
for j in a:
    for i in range(len(l)):
        if j==l[i]:
            s+=str(l[i+1])
print(s)

    
    