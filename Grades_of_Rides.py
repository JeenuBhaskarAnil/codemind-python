h,p,s=map(int,input().split())
if h>50 and p>60 and s>100:
    print("10")
elif h>50 and p>60:
    print("9")
elif p>60 and s>100:
    print("8")
elif h>50 and s>100:
    print("7")
elif h>50 or p>60 or s>100:
    print("6")
else:
    print("5")