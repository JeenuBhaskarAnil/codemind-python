m=input().lower()
n=input().lower()
a=[]
for i in m:
    if i in n and i not in a and i.isalpha():
        a.append(i)
a.sort()
s=''
for i in a:
    s+=i
if len(s)==0:
    print("-1")
else:
    print(s)