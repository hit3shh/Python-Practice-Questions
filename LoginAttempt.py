'''
Q-   Login Attempt Lock

Story:
User gets max 3 attempts. If correct → "Login Successful". 
If 3 wrong → "Account Locked".

Tag: Wipro 2023

Input:
Attempts: wrong, wrong, wrong

Output:
Account Locked

'''
flag=0
for i in range(3):    
    password = input("enter your password: ")

    if password == "12345" :
        print("Login Successful")
        flag = 1
        break
    else: 
        print("Wrong Attempt")

if not flag :
    print("Account Locked!!")

