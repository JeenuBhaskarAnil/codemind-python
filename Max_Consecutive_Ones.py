n=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=str(i)
l=s.split("0")
a=[len(i) for i in l]
print(max(a))