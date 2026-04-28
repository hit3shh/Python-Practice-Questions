'''
Q- you own a parking lot. you have a different pricing for different num of hrs. 
you need to hire a developer to calculate the total bill with the help of a program.:
1- for 1st 2 hrs- 100 rs. per hr

2- for next three hrs- 50 rs. per hr

3- remaining hrs- 25 rs. per hr

'''

hr= float(input("enter num of hrs spend:"))
bill=0

if hr>=0 and hr<=2 :
    bill = hr*100
elif hr>2 and hr<=5:
    bill = 200 + (hr-2)*50
else:
    bill = 350 + (hr-5)*25

print("total bill :",bill)
