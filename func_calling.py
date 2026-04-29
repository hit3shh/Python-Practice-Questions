# call by value: for immutable things in py..

def update(v):
    v="hii"
    print(v)

v1="hello"
update(v1)
print(v1)






# call by reference:  # for mutable things in py..

def update(lst):
    lst[0]=21

list1=[10,20,30,40,50]
update(list1)
print(list1)
