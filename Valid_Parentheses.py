def p(n):
    s="[{()}]"
    st=[]
    for i in n:
        if i in "({[":
            st.append(i)
        else:
            if len(st)==0:
                return False
            if (i==")" and st[-1]=="(") or (i=="]" and st[-1]=="[") or (i=="}" and st[-1]=="{"):
                st.pop()
    if len(st)==0:
            return True
    else:
            return False
for i in range(int(input())):
    n=input()
    a=''
    for i in n:
        if i!="":
            a+=i
    print(p(a))
        
    