'''
 A
CBD
 E
GFH
 I 

'''

n=5    # 5 rows
num=65   # for first char A
for i in range(1,n+1):
    if i%2==0:     # for even rows
        print(chr(num+1),end="")
        print(chr(num),end="")
        print(chr(num+2),end="")

        num+=3  #  increment of +3 for B to E  and F to I :
    else:   # for odd rows:
        print(" ",end="")  # for 1 space at odd rows
        print(chr(num),end="")  # print incremented num  
        num+=1    # increment +1 for A to B then E to F

    print()  # line change  

