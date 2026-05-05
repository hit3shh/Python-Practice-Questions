# OOP :  
# making a class :
'''
syntax:

class Abc:        ##(class is created using 'class' keyword)(first letter of class name should be CAPITAL.)
    ##body

'''

# creating class Bank:

class Bank :
    accno = 0
    name = ""

    # creating constructor  # it shouldbe first function inside class :
    def __init__(self,accno,name):
        self.accno = accno
        self.name = name
        
    # it is show() function we have created for displaying class 
    def show(self):
        print("acc no. :",self.accno)
        print("name: ",self.name)


# creating object of - class Bank :

# b = Bank()   # b is a object of - class bank  # and it is refrencing class Bank 
# print(b.name)  # this prints name available in - class bank

# b.show()  #  this will access show method of -class Bank  



# creating objects for class Bank # using constructers this will assign values 
b = Bank(23456,"Hiteshh")
b2 = Bank(12344,"Sarode")

# using show() func to dispaly created objects wrt class Bank
b.show()
b2.show()

print(b.name)
