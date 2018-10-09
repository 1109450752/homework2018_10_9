class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__e=c
        self.__c=d
        self.__d=e
        self.__f=f
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True
        else:
            return False
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
    def print1(self):
        print (self.getX(),self.getY())
A=LinearEquation(1,2,3,4,5,6)
if A.isSolvable()==True:
    A.print1()