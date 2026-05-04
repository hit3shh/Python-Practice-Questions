
'''
WAP to rotate the elements in a list by k times in anticlock direction

input:
list= [10,20,30,40,50]
k=2

output:
[40,50,10,20,30]

'''

list1 = eval(input("Enter list: "))
k = int(input("enter no. of rotations(k) : "))

for i in range(k):
    item = list1.pop()
    list1.insert(0,item)

print(list1)
