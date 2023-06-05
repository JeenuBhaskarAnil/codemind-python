n=int(input())
l=input().split()
l.sort()
s=[]
for i in l:
    if l.count(i)*i not in s:
        s.append(l.count(i)*i)
s.sort(key=len,reverse= True)
for i in s:
    print(i[0],end=" ")

