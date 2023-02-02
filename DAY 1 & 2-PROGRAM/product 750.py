l=list(map(int,input("enter:").split()))
p=1
for i in l:
    p=i*p
if p<750:
    print("the product is",p)
else:
    print(sum(l))
