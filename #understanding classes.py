#understanding classes
class car:
    def __init__(self,model,year,color,for_sale):
        self.model= model
        self.year= year
        self.color=color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive a  {self.color} {self.model}")


    def stop(self):
        print(f"a {self.color} {self.model} stopped")

    def car_details(self):
        print(f"{self.year} {self.color} {self.model} ")


car1=car("DODGE",2026,"BLUE",False)

#print(car1.model) #outputs DOGE
#print(car1.year)  #outputs 2026
#print(car1.color) #outputs BLUE
#print(car1.for_sale) # outputs FALSE#

car1.drive()
car1.stop()
car1.car_details()

# student details class
class student:

    grade = "A" #class variable outside the constructor 
    number_of_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.number_of_students += 1 # return the number of students

    def student_details(self):
        print("STUDENT DETAILS!!!")
        print(f"NAME : {self.name}")
        print(f"AGE : {self.age}")
        print(f"GRADE : {self.grade}")

student1 = student("anoe",22)
student2 = student("Chikoe",19)

student1.student_details()
print()
student2.student_details()

print(student.number_of_students)



#inheritance

class animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def animal_details(self):
        print("ANIMAL DETAILS")
        print(f"NAME: {self.name}")
        print(f"{self.speak()}")
    


class dog(animal):
    def speak(self):
        print("BARK")

class cat(animal):
    def speak(self):
        print("MEOW")

class Mouse(animal):
    def speak(self):
        print("SQUEEK")

dog1 = dog("skooby")
cat1 = cat("gaffiled")
Mouse1 = Mouse("jerry")

dog1.animal_details()


#dog1.eat()
#cat1.eat()
#Mouse1.eat()

#dog1.sleep()
#cat1.sleep()
#Mouse1.sleep()


#multiple inheritance
class animal:
    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class prey(animal):
    def flee(self):
        print("this animal is fleeing")

class predator(animal):
    def hunt(self):
        print("this animal is hunting")

class rabit(prey):
    pass

class hawk(predator):
    pass

class fish(prey,predator):

    pass

rabbit1 = rabit()
hawk1 = hawk()
fish1 =  fish()

#rabbit1.flee()
#hawk1.hunt()
fish1.sleep()
fish1.hunt()

#class rectangle

class rectangle:

    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth

    def setlength(self):
        newlength = int(input("ENTER NEW VALUE"))
        self.length = newlength
        print("LENGTH UPDATED ")

    def setbredth(self):
        newbredth = int(input("ENTER NEW VALUE"))
        self.bredth = newbredth
        print("BREDTH UPDATED ")

    def getlen(self):
        print(f"LENGTH = {self.length}")

    def getbredth(self):
        print(f"BREDTH = {self.bredth}")

    def area(self):
        
        print(f"AREA = {self.bredth * self.length}" )

    def perimeter(self):
        
        print(f"PERIMETER = {(self.length + self.bredth)* 2}")


    


r1 = rectangle(0,0)

#r1.perimeter()
#r1.area()
#r1.getlen()
#r1.getbredth()

#del r1 *******Used for deleteng objects

r1.setlength()
r1.setbredth()
r1.perimeter()
r1.area()
r1.getlen()
r1.getbredth()

#class student

class student:

    def __init__(self,rollno,name,marklist,stream,percentage,grade,division):
        self.rollno = rollno
        self.name = name
        self.marklist = marklist
        self.stream = stream
        self.percentage = percentage
        self.grade = grade
        self.division = division



    def setmarks(self):
        print("PLEASE ENTER YOUR MARKS")
        marks = []
        for i in range(1,6):
            mark = int(input(f"ENTER MARK {i}:"))

            if mark < 0 or mark > 100:
                print("INVALID INPUT")
                return False

            marks.append(mark)

        self.marklist = marks
        

        total = sum(self.marklist)
        print(f"MARK LIST : {self.marklist}")
        print(f"TOTAL : {total}")
        return True

    def getstream(self):
        print(f"STREAM = {self.stream}")

    def percent(self):
       total = sum(self.marklist)
       self.percentage = (total/500)*100
       print(f"PERCENTAGE = {self.percentage}%")
        

    def gradegen(self):
        print("GRADE")
        if self.percentage >= 90:
            print("A")
        elif self.percentage >= 80:
            print("B")
        elif self.percentage >= 65:
            print("C")
        else:
            print("E")        

s1 = student(101,"ANOE",0,"ARTS",0,0,0)

print("STUDENTS RESULTS")
print(f"ROLL NO: { s1.rollno}")
print(f"NAME : {s1.name}")

if s1.setmarks():
    s1.getstream()
    s1.percent()
    s1.gradegen()

##                             




