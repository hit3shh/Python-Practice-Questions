'''
Q1:
A teacher stored marks but some entries are invalid. remove them and return valid marks.
note:  invalis means -1

example:
input: list=[45,67,-1,89,-1,76]

output:  [45,67,89,76]



Q2:
you have a list of item prices.. calculate total bill after removing free items.
note :  free item mean 0

example:
input:  [100,200,0,50,0,300]
output:  650

'''
#Q1:
list1 = eval(input("enter a list: "))
ele = int(input("enter no: "))
for i in range(len(list1)-1,-1,-1):
    if list1[i] == ele :
        list1.pop(i)

print(list1)




#Q2:
list1 = eval(input("enter a list: "))
bill=0

for i in range(len(list1)):
    bill+=list1[i]

print(bill)

