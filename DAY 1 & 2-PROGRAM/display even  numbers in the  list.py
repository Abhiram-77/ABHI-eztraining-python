size=int(input("size="))

l=[]
for i in range(size):
    ele=int(input("elements="))
    l.append(ele)
    print(l)
for j in l:
    if(j%2==0):
        print(j)
