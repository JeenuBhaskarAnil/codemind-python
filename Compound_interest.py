p,r,t=map(int,input().split())

print("{:.2f}".format(p*(1+r*0.01)**t))