n=input()
l=[]
c=[]
b=['b','a','l','o','n']
for i in n:
    l.append(i)
for i in b:
  if i!='l' and i!='o':
    d=l.count(i)
    c.append(d)
  else:
      d=l.count(i)//2
      c.append(d)
print(min(c))