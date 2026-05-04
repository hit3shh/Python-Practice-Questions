'''
WAP to find 2nd duplicate

'''

list1 = eval(input("enter a list: "))
ele = int(input("enter element: "))
count = 3   # for checking 2 duplicates..

for i in range(list1):
    if list1[i] == ele :
        count -= 1

    if count == 0 :
        print(i)
        break
else: 
    print("Not exist")



