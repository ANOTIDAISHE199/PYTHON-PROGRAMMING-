class person():

    def __init__(self,name,age,city):
          self.name = name
          self.age = age
          self.city = city
      


    def display_details(person):
        print("---------------")
        print("PERSON DETAILS")
        print("---------------")
        print(f"NAME : {person.name}")
        print(f"AGE : {person.age}")
        print(f"CITY : {person.city}")

person1 = person("ANOE",22,"HARARE")
person1.display_details()
