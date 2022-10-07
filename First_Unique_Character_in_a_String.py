n=input()
t=0
for i in range(len(n)):
   if n.count(n[i])==1:
       print(i)
       t=t+1
       break
if t==0:
    print('-1')