# # prime numbers in range 1 to n :

# n=int(input("enter last range: "))

# for i in range(2,n+1):
#     for j in range(2,(i//2)+1):
#         if i%j == 0 :
#             break
#     else:
#         print("prime:",i)



# sum of prime num in range 1 to n :

n= int(input("Enter last range: "))
sum=0
for i in range(2,n+1):
    for j in range(2,(i//2)+1):
        if i%j == 0 :
            break
    else:
        print(i)
        sum+=i

print("sum:",sum)