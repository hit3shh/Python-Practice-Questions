'''
Q-  Dynamic Pricing Engine

Story:
Price increases:
• Demand High → +20% 
• Weekend → +10% 
• Both → cumulative 

Tag: Flipkart 2024

Input:
Base = 1000
Demand = High
Weekend = Yes

Output:
Final Price = 1320

'''

base= int(input("Enter base price: "))
demand= input("demand (high/low): ")
weekend= input("weekend(yes/no): ")

if demand == "high" and weekend == "yes" :
    base = base*1.3
elif demand == "high" :
    base = base*1.2
elif  weekend == "yes" :
    base = base*1.1

print("Final price: ",base)

