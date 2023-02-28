#multi-level inheritance
class grandparents:
    def display(self):
        print("grandparents class")
class parent(grandparents):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing()
