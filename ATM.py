'''
Q- ATM Withdrawal Logic
Story: Withdraw only if:
• Balance ≥ amount
• Minimum balance ₹1000 maintained
Else show reason

Tag: Accenture 2024

Input: Balance = 5000 Withdraw = 4500

Output: Transaction Failed: Minimum balance violation

'''

balance= int(input("Balance in account: "))
amount= int(input("enter withdrawal amount: "))

if balance-amount >= 1000 :
    print("Withdrawal successful.")
else: 
    print("Transaction failed!")

    print("minimum withdrawal violation.   amount= ",balance-amount )