l=input().split()
s=''
for i in l:
    s=s+i
v=0
c=0
d=0
z=''
for i in s:
    z=z+i.lower()
for i in z:
   if i in ('a','e','i','o','u') :
       v+=1
   elif i in ('b','c','d','f','g','j','h','k','l','m','n','q','p','r','s','t','v','w','x','y','z'):
       c=c+1
   else:
       d=d+1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',len(l)-1)