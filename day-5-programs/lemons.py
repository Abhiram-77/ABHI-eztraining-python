def lemon():
    a=int(input("no of lemons avilable:"))
    b=int(input("no of lemons offered 1st:"))
    c=int(input("no of lemons offered 2nd:"))
    d=int(input("no of lemons offered 3rd:"))
    excess=a-(b+c+d)
    print("no of excess lemons available:",excess)
lemon()
