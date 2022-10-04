n=input()
v=input()
c=0
l=[]
for i in range(len(n)):
    l.append(n[i])
for i in range(len(l)):
    if v==str(l[i]):
      print("True")
      c=c+1
      print(i)
      break
if c==0:
    print("False")