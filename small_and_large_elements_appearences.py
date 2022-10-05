l=input().split()
b=""
for i in l:
    b=i+b
print(min(b),b.count(min(b)),max(b),b.count(max(b)))