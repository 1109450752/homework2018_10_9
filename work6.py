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
class xian:
    def __init__(self,x1,y1,x2,y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
    def getshu(self):
        a=self.__y1-self.__y2
        b=self.__x2-self.__x1
        c=-(self.__x1*self.__y2-self.__y1*self.__x2)
        return a,b,c
    def printfangchen(self):
        a,b,c=self.getshu()
        print("{}x {}y {}".format(a,b,c))
A=xian(2,2,0,0)
B=xian(0,2,2,0)
A.printfangchen()
B.printfangchen()
a,b,c=A.getshu()
d,e,f=B.getshu()
print(a,b,c,d,e,f)
A1=LinearEquation(a,b,c,d,e,f)
if A1.isSolvable()==True:
    A1.print1()