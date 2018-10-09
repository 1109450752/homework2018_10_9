class Account:
    def __init__(self,id=0,balance=100,rate=0):
        self.__id= int(id)
        self.__balance=float(balance)
        self.__rate=float(rate)
    def getMouthlyInterestRate(self):
        #print(self.__rate/100/12)
        return self.__rate/100/12
    def getMouthlyInterset(self):
        #print(self.__balance*self.getMouthlyInterestRate())
        return self.__balance*self.getMouthlyInterestRate()
    def withdrw(self,a1):
        self.a1=a1
        self.__balance=self.__balance - a1
    def deposit(self,a2):
        self.a2=a2
        self.__balance = self.__balance + a2
    def print1(self):
        print("{},{},{}%,{}".format(self.__id,self.__balance ,self.getMouthlyInterestRate()*100,self.getMouthlyInterset()))
A1=Account(1122,20000,4.5)
A1.print1()
A1.withdrw(2500)
A1.print1()
A1.deposit(3000)
A1.print1()



