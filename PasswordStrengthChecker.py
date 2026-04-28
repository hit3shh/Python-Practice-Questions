'''
Password Strength Checker

Story:
Password must have:
• ≥8 chars 
• 1 digit 
• 1 uppercase 
• 1 special char
Else show missing criteria 

Tag: Tech Mahindra 2024

Input:
Password = Abc123

Output:
Weak Password: Missing special character, length < 8

'''

password = input("enter password:")

hasUpper = False
haslower = False
hasDigit = False
hasSymbol = False
hasLen = len(password) >=8

for i in password :
    if i.isupper():
        hasUpper=True
    elif i.islower():
        hasLower=True
    elif i.isdigit():
        hasDigit=True
    else:
        hasSymbol=True


if hasUpper and hasDigit and hasLen and hasSymbol :
    print("Strong")
else:
    print("Weak")

    