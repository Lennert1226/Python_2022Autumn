'''
def mul(a,b):
    return a*b
ya = mul(10,1)
print(ya)
'''
''''''
class Car:    #建立類別class
    pass
benz = Car()    #建立物件Object
print(isinstance(benz, Car))     #判斷類別class與物件object的關係

benz = Car()   #建立Car類別的物件

#負責儲存物件object的資訊
benz.color = "blue"    #顏色屬性
benz.seat = 4    #座位屬性
#呼叫物件的屬性值
print(benz.color)    #執行結果:blue
print(benz.seat)    #執行結果:4

#Constructor
class Car:
    #建構式
    def __init__(self, color, seat):   #雖建構式有三個參數值，但只需傳入兩個參數，因第一個self參數，Python編譯器會自動把目前物件的參數(benz)傳給建構式
        self.color = color    #顏色屬性
        self.seat = seat    #座位屬性
benz = Car("blue", 4)    #產生物件benz，同時生成color和seat屬性，並初始化屬性值

class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
person1 = FullName("Andy","Wang")
person2 = FullName("Lulu","Cheng")
print(person1.firstname,person1.lastname)
print(person2.firstname,person2.lastname)

class Car:
    #建構式
    def __init__(self, color, seat):   #雖建構式有三個參數值，但只需傳入兩個參數，因第一個self參數，Python編譯器會自動把目前物件的參數(benz)傳給建構式
        self.color = color    #顏色屬性
        self.seat = seat    #座位屬性

    def move(self,meter):
        print("My car moves "+str(meter)+" meters")

    def printAttribute(self):
        print("My car's color is "+self.color)
        print("My car has "+str(self.seat)+" seat")


benz = Car("blue",4)
benz.move(5)
benz.printAttribute()


class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printAttribute(self):
        print("My name is "+str(self.firstname)+", "+str(self.lastname))
        


person1 = FullName("Andy","Wang")
person1.printAttribute()

person2 = FullName("Lulu","Cheng")
person2.printAttribute()

class Shoes:
    def __init__(self,gender,size):
        self.gender = gender
        self.size = size
    
    def printAttribute(self):
        print("I am a "+str(self.gender)+", and my shoe size is US "+str(self.size))

person1 = Shoes("boy","9")
person1.printAttribute()
person2 = Shoes("girl","7")
person2.printAttribute()

class People:
    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age
    
    def printAttribute(self):
        print("The height is "+str(self.height)+"cm"+", weight is "+str(self.weight)+"kg"+", and the age is "+str(self.age)+" years old")
person1 = People("170","60","40")
person1.printAttribute()
person2 = People("190","70","17")
person2.printAttribute()
person3 = People("178","74","48")
person3.printAttribute()
person4 = People("162","41","12")
person4.printAttribute()