'''
WAP to find 2md largest and 3rd smallest number in a list of elements 

'''

list1= eval(input("enter a list: "))

largest = float('-inf')
second = float('-inf')

small = float('inf')
second_small = float('inf')
third_small = float('inf')

for i in list1 :
    if i >= largest :
        second=largest
        largest=i
    elif i > second  :
        second=i


    if i <= small :
        second_small = small
        third_small = second_small
        small = i
    elif i<=second_small :
        third_small = second_small
        second_small = i
    elif i <= third_small :
        third_small = i 


print("second largest: ",second)
print("third smallest: ", third_small)




