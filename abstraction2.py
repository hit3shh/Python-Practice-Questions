# abstract data structure:  which do not has there own implementation... they are depending on oothers
# example: linked list.. they are depend on arrays etc..

# concrete data str : they are implemented on there own.. donot depends on any other data str
# example : such as Arrays..


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay():
        pass
    
class UPI(Payment) :   # it is a single level inheritance..# UPI class inherits Payment class
    def pay(self):
        print("payment done by UPI!!")

class CC(Payment) :  
    def pay(self):
        print("payment done by Credit Card")

class DC(Payment) :  
    def pay(self):
        print("payment done by Debit card!!")


if __name__ == "__main__" :
    u = UPI()
    u.pay()

    u=CC()
    u.pay()
