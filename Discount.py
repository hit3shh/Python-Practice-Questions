'''
Q- Discount Eligibility

Story:
1- If amount ≥5000 → 20% discount.

2- If ≥3000 → 10%

3- Else → no discount

4- If user is premium → extra 5%

Tag: Capgemini 2022

Input: Amount = 6000 Premium = Yes

Output: Final Amount = 4500

'''

amount= int(input("enter total amount: "))
premium = input("premium customer(yes/no): ")

if amount >= 5000 :
    amount= 0.8*amount

elif amount >= 3000:
    amoount = 0.9*amount

if premium == "yes":
    amount = 0.95*amount

print("total amount after discount: ", amount)

