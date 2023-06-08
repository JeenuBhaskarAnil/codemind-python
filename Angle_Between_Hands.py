n=input().split(":")
h=int(n[0])
m=int(n[1])
a=abs(5.5*m-30*h)
l=[a,360-a]
print(min(l))