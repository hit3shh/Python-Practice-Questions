# # # check pallindrome string:

# # # using slicing:
# # s= input("enter a string: ")

# # s_rev = s[::-1]

# # if s==s_rev :
# #     print("pallindrome")
# # else:
# #     print("not pallindrome")



# # Using function:
# def pallindrome(str):
#     n=len(str)

#     for i in range(0,((n-1)//2)+1):
#         if str[i]!=str[n-1-i]:
#             print(str, "Not Pallindrome")
#             return     # works same as break
#     print(str, "Pallindrome")


# pallindrome("abbca")
# pallindrome("abca")
# pallindrome("abba")





# check frequency of each character in string:

def CountFrequency(s):
    dict={}
    for i in s:
        if i in dict :
            dict[i]+=1
        else:
            dict[i]=1
    
    return dict

# s=input("enter a string: ")

# print(CountFrequency(s))


# check Anagram strings  ( all strings contains same num of characters)

def anagram(s1,s2):
    d1=CountFrequency(s1)
    d2=CountFrequency(s2)

    for i in d1:
        if i not in d2 or d1[i] != d2[i] :
            return False 
        else:
            d2.pop(i)   # if both conditions of if gets False means i is in d2 and also in d1,d2 both :
            
    if len(d2.keys()) == 0 :
        return True
    else:
        return False
    
s1 = input("enter a string: ")
s2 = input("enter a string: ")

print(anagram(s1,s2))






