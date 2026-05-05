class Phone :

    __phoneId = 0
    __os = ""
    __brand = ""
    __price = 0

    def __init__(self,phoneId,os,brand,price):
        self.__phoneId = phoneId
        self.__os = os
        self.__brand = brand
        self.__price = price

    def getphoneId(self):
        return self.__phoneId
    def setphoneId(self,phoneId):
        self.__phoneId = phoneId
    
    def getos(self):
        return self.__os
    def setos(self,os):
        self.__os = os
    
    def getbrand(self):
        return self.__brand
    def setbrand(self,brand):
        self.__brand = brand
    
    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price = price

    
class Solution:

    @staticmethod
    def findPriceForGivenBrand(lst,brand):
        sum = 0
        for phone in lst :
            if phone.getbrand() == brand :
                sum += phone.getprice()
        return sum

    @staticmethod
    def getPhoneIdBasedOnOs(lst,os):
        for phone in lst :
            if phone.getos() == os and phone.getprice() >= 50000 :
                return phone
            else:
                return None
            
if __name__ == "__main__" :

    lst=[]

    n = int(input())
    for i in range(n) :
        phoneId = int(input())
        os = input()
        brand = input()
        price = int(input())

        p = Phone(phoneId,os,brand,price)
        lst.append(p)

    brand = input()
    os = input()

    sum = Solution.findPriceForGivenBrand(lst,brand)
    phone = Solution.getPhoneIdBasedOnOs(lst,os)

    if sum > 0 :
        print(sum)
    else:
        print("The Given Brand Is Not Available")

    if phone != None :
        print(phone.getphoneId())
    else:
        print("No phones available with specified os and price range")



    
