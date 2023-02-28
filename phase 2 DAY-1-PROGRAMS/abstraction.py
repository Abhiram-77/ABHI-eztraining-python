import abc from ABC,abstractmethod
class abstraction(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None

class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def display(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()
    
