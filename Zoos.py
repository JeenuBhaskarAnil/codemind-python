n=input()
z=0
o=0
for i in n:
    if i is 'z':
        z=z+1
    else:
        o=o+1
if o/2==z:
    print("Yes")
else:
    print('No')
