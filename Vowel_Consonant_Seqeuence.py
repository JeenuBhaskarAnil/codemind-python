n=input()
v="aeiou"
l=["x"]
for i in n:
    if i in v and l[len(l)-1]!="V":
        l.append("V")
    elif l[len(l)-1]!="C":
        l.append("C")
l=l[1:]
x=''
for i in l:
    x+=i
print(x)
    