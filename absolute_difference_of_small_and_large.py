l=input().split()
k=[]
for i in l:
    k.append(ord(max(i))-ord(min(i)))
for i in k:
    print(i,"",end="")