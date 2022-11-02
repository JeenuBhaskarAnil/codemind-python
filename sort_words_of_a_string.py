z=input().split()
for i in z:
    l=[]
    s=[]
    d=''
    for j in i:
        if j.isalnum():
            l.append(j)
        else:
            s.append(j)
            s.append(i.index(j))
    l.sort()
    for j in range(0,len(s),2):
        l.insert(s[j+1],s[j])
    for j in l:
        d+=str(j)
    print(d,end=' ')
        
    
