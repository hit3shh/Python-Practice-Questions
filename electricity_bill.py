'''
Q- you need to calculate total electricity bill based on num of units.

1-   for 0-100 units : rs. 1.5 per unit

2-   for 101-200 units : rs. 3.5 per unit

3-   for remaining : rs. 5 per unit

you need to add rs. 50 as fixed charge.

if bill exeeds rs 2000 then add surplus charge of 10% of total bill. 

'''

no_of_units= int(input("number of units:"))

bill=50

if no_of_units <100:
    bill+= no_of_units*1.5

elif no_of_units<200:
    bill+= ((100*1.5)+ (no_of_units-100)*3.5)

else:
    bill+= ((100*1.5)+(100*3.5)+(no_of_units-200)*5)

if  bill>2000:
    bill +=  bill*0.1
    print("total bill:",bill)
else:
    print("total bill:",bill)

