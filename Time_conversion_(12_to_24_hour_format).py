n=input()
h=(n[:2])
s=''
a=["12 AM","01 AM","02 AM","03 AM","04 AM","05 AM","06 AM","07 AM","08 AM","09 AM","10 AM","11 AM","12 PM","01 PM","02 PM","03 PM","04 PM","05 PM","06 PM","07 PM","08 PM","09 PM","10 PM","11 PM"]
b=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
for i in range(len(a)):
    #print(n[6:8],a[i][3:5])
    if a[i][:2]==n[:2] and n[6:8]==a[i][3:5]:
        s=b[i]+n[2:5]
print(s)
        