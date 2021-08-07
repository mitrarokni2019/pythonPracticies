class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        
    def getColor(self):
        return self.color

    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name

    def getCharOfName(self, charIndex):
        return self.name[charIndex]

    def swapNameWithColor(self):
        temp = self.name
        self.name = self.color
        self.color = temp

class Garage:
    def __init__(self, car: Car):
        self.car = car

car1 = Car("Red", "Jian")
car1.setName("citroen")
car1.swapNameWithColor()
print(car1.getName())
print(car1.getCharOfName(2))
print(car1.getColor())

garage1 = Garage(car1)
print(garage1.car)