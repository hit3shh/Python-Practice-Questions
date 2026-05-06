# polymorphism:   "Many forms" :

# types: 
    #1- method overloading
    #2- method overriding

# addition.py:

# class A:
#     def start(self):
#         print("A statrted!!")

# class B(A):
#     def start(self):
#         print("B started!!")

# if __name__ == "__main__" :
#     b = B()
#     b.start()    # runs for B 


# so we use super func:  this is used in child class to access methods of parent class first than child class ..

class A:
    def start(self):
        print("A statrted!!")

class B(A):
    def start(self):
        super().start()   # it is used to access parent class first..
        print("B started!!")

if __name__ == "__main__" :
    b = B()
    b.start()    # runs for A than B


