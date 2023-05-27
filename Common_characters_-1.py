li=input().lower().split()
l=li[1:len(li)]
r=""
for i in li[0]:
    s=0
    for j in l:
        if i in j:
            s+=1
            j=j[0:j.index(i)]+j[j.index(i)+1:len(j)]
    if len(l)==s:
        r+=i
if len(r)!=0:
    print(r)
else:
    print("-1")