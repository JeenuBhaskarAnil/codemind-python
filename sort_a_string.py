def so(n):
    temp=''
    v=""
    for i in n:
        if i.isalnum():
            temp+=i
    temp=list(temp)
    temp.sort()
    n=list(n)
    k=0
    a=[]
    for i in n:
        if i.isalnum():
            a.append(temp[k])
            k+=1
        else:
            a.append(i)
    s=''
    for i in a:
        s+=i
    return s
print(so(input()))