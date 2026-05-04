'''
WAP to find the nth largest or nth smallest num 

'''


list1 = eval(input("enter a list: "))
n = int(input("enter n: "))

list1.sort()

print(f"{n}th largest: ", list1[-n])
print(f"{n}th smallest: ", list1[n-1])

