class Institution:
    __institutionId = 0
    __institutionName = ""
    __noOfStudentPlaced = 0
    __noOfStudentCleared = 0
    __location = ""
    __grade = ""

    def __init__(self,institutionId,institutionName,noOfStudentPlaced,noOfStudentCleared,location,grade):
        self.__institutionId = institutionId
        self.__institutionName = institutionName
        self.__noOfStudentPlaced = noOfStudentPlaced
        self.__noOfStudentCleared = noOfStudentCleared
        self.__location = location
        self.__grade = grade

    def getinstitutionId(self):
        return self.__institutionId
    def setinstitutionId(self,institutionId):
        self.__institutionId = institutionId
    
    def getinstitutionName(self):
        return self.__institutionName
    def setinstitutionName(self,institutionName):
        self.__institutionName = institutionName

    def getnoOfStudentPlaced(self):
        return self.__noOfStudentPlaced
    def setnoOfStudentPlaced(self,noOfStudentPlaced):
        self.__noOfStudentPlaced = noOfStudentPlaced
    
    def getnoOfStudentCleared(self):
        return self.__noOfStudentCleared
    def setnoOfStudentCleared(self,noOfStudentCleared):
        self.__noOfStudentCleared = noOfStudentCleared

    def getlocation(self):
        return self.__location
    def setlocation(self,location):
        self.__location = location

    def getgrade(self):
        return self.__grade
    def setgrade(self,grade):
        self.__grade = grade


class Solution:

    @staticmethod
    def FindNumClearancedByLoc(self,lst,location):

        total=0
        for institution in lst :
            if institution.getlocation == location :
                total += institution.getnoOfStudentCleared
        return total
        
    @staticmethod
    def UpdateInstitutionGrade(self,InstitutionName,lst):

        for institution in lst:
            if institution.getinstituteName == InstitutionName :
                
                return institution
    
        return None
    

if __name__ == "__main__" :

    n = 4
    lst=[]

    for i in range(n):
        institutionId =int(input())
        institutionName = input()
        noOfStudentPlaced =int(input())
        noOfStudentCleared =int(input())
        location = input()

        
        



