a=10
b=0
try:
    print("resources open")
    print(a/b)
except Exception as e:
    print("don't give second number as zero",e)
finally:
    print("resource closed")
