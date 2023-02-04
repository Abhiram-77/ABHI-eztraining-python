class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \nName: %s" % (self.id,self.name))

Emp1=Employee("john",101)
Emp2=Employee("david",102)

Emp1.display()
Emp2.display()




    
