def p(n):
    s="[{()}]"
    st=[]
    for i in n:
        if i in "({[":
            st.append(i)
        else:
            if len(st)==0:
                return n.index(i)+1
            if (i==")" and st[-1]=="(") or (i=="]" and st[-1]=="[") or (i=="}" and st[-1]=="{"):
                st.pop()
            else:
                return n.index(i)+1
    if len(st)==0:
            return 0
    else:
            return len(n)+1

n=input()
#a=''
#for i in n:
#    if i!="":
 #       a+=i
print(p(n))
    
    