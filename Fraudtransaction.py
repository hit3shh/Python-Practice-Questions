'''
Q-  Fraud Transaction Detection

Story:
Transaction flagged if:
• Amount > ₹50,000 AND location mismatch 
• OR >3 transactions in 1 min 

Tag: Amazon 2024

Input:
Amount = 60000
LocationMatch = No
Transactions = 1

Output:
Fraud Detected

'''
amt = int(input("Enter transaction amount: "))
num_of_transaction = int(input("enter num of transactions: "))

if amt > 50000 or num_of_transaction>3 :
    print("fraud detected")
else:
    print("legal transaction.")