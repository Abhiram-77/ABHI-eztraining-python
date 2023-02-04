a=int(input("enter a number:"))
b=int(input("enter a number:"))
try:
    print(a/b)
except Exception as e:
    print("please note,number cant be divided by zero",e)
    print("bye")
