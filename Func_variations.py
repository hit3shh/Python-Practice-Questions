# 1st variation:  No return, No Arguments

def greet():
    print("Hello!!")

greet()


#2nd variation:  No return, with arguments

def greetings(name):
    print(name,"hiii", sep="@")

greetings("Hiteshh")


#3rd varistion:    With Return, No arguments

def greet3():
    return "sab changa si!!"

print(greet3())


# 4th variation:   With return, with aarguments 

def greet4(name):
    return "Good morning!" +name

print(greet4("Hiteshh"))

