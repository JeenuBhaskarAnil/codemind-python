from itertools import permutations
n=input()
l=list(permutations(n))
ll=[list(i) for i in l]
for l in ll:
    s=''
    for i in l:
        s+=i
    print(s)