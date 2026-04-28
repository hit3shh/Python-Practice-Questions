'''
Q- Odd-Even Game

Story:
Game checks numbers till 0 is entered. ..Count odd & even numbers.

Tag: Cognizant 2023

Input: 2 3 4 5 0

Output: Even = 2 | Odd = 2

'''

num = int(input("enter a number: "))
even,odd = 0,0

while(num):
    if num%2 == 0 :
        even+=1
    else:
        odd+=1
    
    num= int(input("enter number: "))

print("Even count:", even)
print("Odd count:", odd)

