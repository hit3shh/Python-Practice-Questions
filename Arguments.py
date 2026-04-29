# #1-   positional arguments:   # arguments are accepted in same sequence we have provided ..

# def profile(name,age):
#     print("name:",name)
#     print("age:",age)
#     print(name,age)

# profile(21,"hiteshh")


# ######################################################

# ######################################################
# print()
# print()



# #2-   Default Arguments:      #  always show by default value of arg untill we pass/update anything

# def profile(name,age,alive="yes"):    # alive argument is default arg..  its always "yes" by default....
#     print("name:",name)
#     print("age:",age)
#     print("alive:",alive)
#     print(name,age,alive)

# profile("hiteshh",21)   #by default it shows "alive:yes"
# profile("anmol",210,"no")     # it shows "alive:no"  bcz we passed a value


# ######################################################

# ######################################################
# print()
# print()


# #3-   Keyword arguments:    we use keywords while giving inputs so values assign as required

# def profile(name,age):
#     print("name:",name)
#     print("age:",age)
#     print(name,age)

# profile(age=21,name="hiteshh")



# ######################################################

# ######################################################
# print()
# print()

# #4-  Multiple Argumments:   # used as *args : when we dont know num of arguments to be used:   also known as astric(*) arguments  # all arguments are in form of tuples ..written inside (...)

# def add(*num):  # we can use this function for multiple numbers.. 2,4,5,7,etc...
#     sum=0
#     for i in num:
#         sum+=i
#     print(num,"sum:",sum)

# add(5,10,15)
# add(34,11,17,98,44,11,57)  
# add(9)



# ######################################################

# ######################################################
# print()
# print()



# #5-   Multiple Keywords arguments:    #combination of multiple and keyword agruments  # used as **kwargs    # all args in form of dictionary by default..

# def profile(**data):
#     for i in data:
#         print(data[i])  # gives values


#     print(data)  # prints dictionary

# profile(name="Hiteshh",age=21,phone=7898842270)


