# encapsulation :-  # using getter and setter functions :

'''
 # private variables are createed suing double underscore( __ ) in prefix   
 # we cant set values of private variables.. so we need setter func to set values and getter func for getting them

'''
class Bank:
    __accno = 0   
    __name = ""  
    __balance = 0

    # constructer :
    def __init__(self,accno,name,balance):
        self.__accno = accno
        self.__name = name
        self.__balance = balance


    # we need getter and setter for accessing private variables :

    # getter function for acc no
    def getaccno(self):
        return self.__accno

    # setter func for acc no
    def setaccno(self,accno):
        self.__accno = accno

    # getter func for name
    def getname(self):
        return self.__name
    
    #setter func for name
    def setname(self,name):
        self.__name = name

    # getter for balance
    def getbalance(self):
        return self.__balance
    
    # setter func for balance
    def setbalance(self,balance):
        self.__balance = balance

b = Bank(0,"",0)


# set acc no = 12345 and get it(print)
b.setaccno(12345)
print(b.getaccno())  # access getter function of acc no

# set name = "Hiteshh" and get it
b.setname("Hiteshh")
print(b.getname())

# set balance = 5000 and get it
b.setbalance(5000)
print(b.getbalance())





### name mangling:   name ka ghotala :  private vairables arre not private really.. they can be accesed somehow in python : 
## this way of data access is not allowed in real cases

print(b._Bank__accno)   # it is accessible in this condition:   _Bank__accno



