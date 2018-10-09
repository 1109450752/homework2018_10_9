class UML:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b
    def getArea(self):
        print (self.a*self.b)
    def getPerimeter(self):
        print ((self.a+self.b)*2)
UML().getArea()
p=UML(4,40)
p.getArea()
p.getPerimeter()
UML(3.5,35.7).getArea()
UML(3.5,35.7).getPerimeter()