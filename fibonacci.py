n=int(input())
print(0,"",end="")
print(1,"",end="")
print(1,"",end="")
a=1
b=2
for i in range(n-3):
    print(b,"",end="")
    c=a+b
    a=b
    b=c
