def so(n):
    temp=''
    v="AEIOUaeiou"
    for i in n:
        if i not in v:
            temp+=i
    temp=list(temp)
    temp.sort()
    n=list(n)
    k=0
    a=[]
    for i in n:
        if i not in v:
            a.append(temp[k])
            k+=1
        else:
            a.append(i)
    s=''
    for i in a:
        s+=i
    return s
        
        
    
            
for l in input().split():
    print(so(l),end=" ")