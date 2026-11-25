class Animal():
    def __init__(self):
        pass
        
    def infor(self):
            print("DOMESTIC ANIMAL")

class dog(Animal):

    def eats(self,):
        super().__init__()
        print("EVERYTHING ALIVE")

    def sounds(self):
        print("BARKS")



dog1 = dog()

dog1.infor()