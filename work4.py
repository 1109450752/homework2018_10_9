class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color="blue",on=False):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def print1(self):
        print (self.__speed,self.__radius,self.__color,self.__on)
A=Fan(Fan.FAST,10,"yellow",True)
B=Fan(Fan.MEDIUM,5,"blue",False)
A.print1()
B.print1()