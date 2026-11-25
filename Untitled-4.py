###super(): function used in a child classs to call methods of a parent class(superclass).....
###allows you to extend the functionality of the inherited methods
class shape:
     def __init__(self,color,is_filled):
         self.color=color
         self.is_filled = is_filled
         
class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

class square(shape):
    def __init__(self,color,is_filled,width):
            super().__init__(color,is_filled)
            self.width = width

class triangle(shape):
   def __init__(self,color,is_filled,width,length):
           super().__init__(color,is_filled)
           self.width = width
           self.length = length

c1 = circle("RED",True,5)
print(c1.color)
print(c1.radius)
print(c1.is_filled)

####polymorphism : 
from abc import ABC, abstractmethod

class shape:

    @abstractmethod
    def area(self):
         pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    
class square(shape):
    def __init__(self,side):
       self.side = side

    def area(self):
        return self.side * self.side

class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


shapes = [circle(4),square(5),triangle(6,7)]

for s in shapes:
     print(s.area())


###duck typing: another way to achieve polymorphism besides inheritance
# object must have minimum necessary attributes/methods 
# if it looks like a duck and quacks like a duck it must be a duck
# 
class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("Buck")
    
class cat(animal):
    def speak(self):
        print("meow!")

class cars():
    alive = False

    def speak(self):
        print("Honk!")

animals = [dog(),cat(),cars()]

for a in animals:
    a.speak()
    print(a.alive)


##static method = a method that belongs to a class rather than  any object from that class

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position


    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager","cashier","cook","janotor"]
        return position in valid_positions



print(Employee.is_valid_position("cashier"))










