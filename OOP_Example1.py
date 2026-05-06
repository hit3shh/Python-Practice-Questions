'''
Question: 1
Create a class TravelAgencies with below attributes:

regNo – int
agencyName – String
pakageType – String
price – int
flightFacility – boolean

Write getters, setters for the above attributes . Create constructor which takes parameter in the above sequence.

Create class Solution with main method. Implement two static methods – findAgencyWithHighestPackagePrice and 
agencyDetailsforGivenIdAndType in Solution class.

findAgencyWithHighestPackagePrice method:

This method will take array of TravelAgencies objects as an input parameter and return the highest package 
price from the given array of objects.

agencyDetailsForGivenldAndType method:

This method will take three input parameters -array of TravelAgencies objects, int parameter regNo and String
parameter packageType. The method will return the TravelAgencies object based on below conditions.

FlightFacility should be available.
The input parameters(regNo and packageType) should matched with the regNo and packageType of TravelAge.0ncies object.
If any of the above conditions are not met, then the method should return null. Note : Same Travel agency can 
have more than one package type. Travel agency and package type combination is unique. All the searches should 
be case insensitive.

The above mentioned static methods should be called from the main method.


For findAgencyWithHighestPackagePrice method – The main method should print the highestPackagePrice as it is. 
For agencyDetailsForGivenldAndType method -The main method should print the AgencyName and price of the returned 
object.The AgencyName aT
Input
---------
4

123
A2Z Agency
Platinum
50000
true

345
SSS Agency
Gold
30000
false

987
Cox and Kings
Diamond
40000
true

888
Global Tours
Silver
20000
false

987
Diamond
-------------------------------
Output
-------------------------------
50000
Cox and Kings:40000

'''

class TravelAgencies :

    __regNo = 0
    __agencyName = "" 
    __packageType = ""
    __price = 0
    __flightFacility = False

    def __init__(self,regNo,agencyName,packageType,price,flightFacility):
        self.__regNo = regNo
        self.__agencyName  = agencyName
        self.__packageType = packageType
        self.__price = price
        self.__flightFacility = flightFacility

    def getregNo(self):
        return self.__regNo
    def setregNo(self,regNo):
        self.__regNo = regNo

    def getagencyName(self):
        return self.__agencyName
    def setagencyName(self,agencyName):
        self.__agencyName = agencyName

    def getpackageType(self):
        return self.__packageType
    def setpackageType(self,packageType):
        self.__packageType = packageType

    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price = price

    def getflightFacility(self):
        return self.__flightFacility
    def setflightFacility(self,flightFacility):
        self.__flightFacility = flightFacility

    
class Solution :

    # for static methos we use this before defining method :  @staticmethod
    @staticmethod   # without creating objects we can call static methods
    def findAgencyWithHighestPackagePrice(lst):
        max = 0
        for agency in lst :
            if agency.getprice() > max :
                max = agency.getprice()

        return max 
    


    @staticmethod
    def agencyDetailsForGivenIdAndType(lst,regno,packagetype):
        
        for agency in lst :
            if agency.getflightFacility() and agency.getregNo() == regno and agency.getpackageType() == packagetype :
                return agency
        
        return None 

if __name__ == "__main__" :
              #  it is main method  # always created at last   # we dont have main function in python.. this is main indentation here.. 
    n = int(input())
    lst=[]

    for i in range(n):
        regno = int(input())
        agencyName = input()
        packageType = input()
        price = int(input())
        flightFacility = bool(input())

        agency = TravelAgencies(regno,agencyName,packageType,price,flightFacility)

        lst.append(agency)

    regno = int(input())
    packagetype = input()

    # Output
    print("-------------------------------------------------\nOutput\n-------------------------------------------------")

    max = Solution.findAgencyWithHighestPackagePrice(lst)
    agency = Solution.agencyDetailsForGivenIdAndType(lst,regno,packagetype)
    print(max)
    print(agency.getagencyName(),':',agency.getprice())



