# # # # # List :  It is a mutable datatype in python

# # # # lst = [10,20,30]
# # # # l = lst

# # # # print(l)  # same as lst  [10,20,30]
# # # # print(lst) # [10,20,30]

# # # # l[0] = 15

# # # # print(l)   # 10 changes to 15  [15,20,30]
# # # # print(lst)  # [15,20,30]   due to referencing 


# # # lst=[10,20,30]
# # # l=list(lst)  # use list()  function for copying lst to l  .. changes in l do not affect lst

# # # print(l)
# # # print(lst)

# # # l[0] = 15

# # # print(l)
# # # print(lst)

# # lst = list(input("enter a list: "))
# # print(lst)   # it will seperate input- character wise   - monday as : m,o,n,d,a,y  

# # lst2= eval(input("enter a list:"))  # eval() can take any type of input..  it is used where we dont know what kind of input will be entered by user
# # print(lst2)   # enter list in [ ]  


# # append( ) add value at end of list
# lst=  [10,20,30]

# lst.append(100)  # adds at last 
# lst.insert(2,200)  # adds 200 at 2nd index
# # lst.append([90,80,70])  # adds list at end as a nested list.. whole at a time
# # lst.extend([33,44,55])  # extends collections in list.. one by one


# # lst.pop(2)  # remove element from 2nd  index.. if not given any inndex- removes at last..
# # del lst[0:2]  # delete elemnts from index 0 to 2  # we use slice here  [0:2]  deletes elementss at index 0,1
# # lst.remove(33) # delete 33 from lst   # specific value
# # # lst.clear()  # used to clear list.. whole elements are deleted 

# lst.sort(reverse=True)   # .sort( ) is method of list.. cant be called withourt object 

# lst2 = [5,1,2,7,4,10,2]
# # lst3= sorted(lst2) # sorted( )  is a function  .. it sorts list and stores in new list.. no changes reflects in original list...
# lst3= sorted(lst2, reverse=True) # reverse is alloweed here also..

# print(lst3)



lst4 = [1,2,3]

print(lst4)
print(lst4 * 2)  # replicate lst4 two times in same order  1,2,3,1,2,3

