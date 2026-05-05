# Abstraction in oop :

class Meal :
    def __cookRajma(self):
        print("Rajma Prepared")
    
    def __cookRoomaliRoti(self):
        print("Roomali Roti Prepared")

    def __cookRice(self):
        print("Rice prepared")

    def __prepareSalad(self):
        print("salad prepared")

    def __Sweet(self):
        print("sweet prepared")

    def cookMeal(self):
        self.__cookRajma()
        self.__cookRice()
        self.__cookRoomaliRoti()
        self.__prepareSalad()
        self.__Sweet()


if __name__ == "__main__" :
    m = Meal()
    m.cookMeal()

