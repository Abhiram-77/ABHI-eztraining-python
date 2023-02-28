class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1")
class child2(parent):
    def c2show(self):
        print("child2")
class kid1(child1):
    def k1display(self):
        print("kid1 class")
class kid2(child1):
    def k2display(self):
        print("kid2 class")
class kidd1(child2):
    def k1show(self):
        print("kidd1 class")
class kidd2(child2):
    def k2show(self):
        print("kidd2 class")
c1=kid1()
c1.k1display()
c1.c1show()
c1.pdisplay()
c2=kid2()
c2.k2display()
c2.c1show()
c2.pdisplay()
c3=kidd1()
c3.k1show()
c3.c2show()
c3.pdisplay()
c4=kidd2()
c4.k2show()
c4.c2show()
c4.pdisplay()

        

        
