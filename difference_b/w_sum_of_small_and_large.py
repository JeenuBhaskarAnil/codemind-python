l=input().split()
k=[]
h=[]
for i in l:
    k.append(ord(max(i)))
    h.append(ord(min(i)))
print(sum(k)-sum(h))