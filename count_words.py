l=input().split()
c=0
for i in l:
    if i[0].lower() in ('a','e','i','o','u') and i[len(i)-1].lower() not in ('a','e','i','o','u'):
        c=c+1
print(c)