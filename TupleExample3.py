'''
WAP to rotate elements by  k times in anticlockwise direction keeping m elements constant at the left side.

'''

list1 = eval(input("Enter list: "))
k = int(input("enter no. of rotations(k) : "))
m = int(input("enter no of constant elements at left: "))

for i in range(k):
    item = list1.pop()
    list1.insert(m,item)


print(list1)

