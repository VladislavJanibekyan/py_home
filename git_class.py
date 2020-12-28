class Car: #class Car(): class Car(object):
    brand = "BMW"
    year = 2019
    color = "red"
    def presentation(self):
        return self.brand, self.year, self.color
bmw = Car()

bmw.brand = "bmw"
mercedes = Car()
mercedes.brand = "mercedes"
print(bmw.presentation())
print(mercedes.presentation())

print(Car.presentation(bmw))
print(type(bmw))
print(type(bmw.brand))
print(type(bmw.year))
print(bmw.year)

#bmw.year = 2018
print(bmw.year)
print(Car.year)

Car.year = 15 

print(bmw.year)

class Car:
    def __init__(self,brand="bmw",year= 2010,color = "black"):
        self.brand_name = brand
        self.year = year
        self.color = color
    def presentation(self):
        return self.brand, self.year, self.color




a = Car("Bmw",201,12)
b = Car()
print(a.color)
print(b.__dict__)


class Fruit():
    def __init__(self,taste,shape,price,color):
        self.taste = taste
        self.shape = shape
        self.price = price
        self.color = color
    def presentation(self):
        return f"this is a fruit which is {self.taste}, the shape is {self.shape}, the price is {self.price} and the color is {self.color}"


apple = Fruit("sweet","round",20,"red")
mandarin = Fruit("sweet","round",32,"orange")
print(mandarin.presentation())
print(mandarin.__dict__)

print(apple.presentation())
print(apple.__dict__)















































