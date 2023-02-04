#variables and var.access i9n class and method
class computer():
    a=10
    b=20
    print("classs variable inside class",a)

    def config(self):
        c=100
        print("instance access",self.b)


lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config()
