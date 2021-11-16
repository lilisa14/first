class Friends:
    name = ""
    age = ""
    city = ""
    hair = ""
    eyes = ""
    hobby = ""

    def __init__(self, name, age, city, hair, eyes, hobby):
        self.name = name
        self.age = age
        self.city = city
        self.hair = hair
        self.eyes = eyes
        self.hobby = hobby

    def info(self):
        print("Ваш друг ", self.name)
        print("Его возраст - ", self.age)
        print("Он из города ", self.city)
        print("Цвет его волос - ", self.hair)
        print("Цвет его глаз - ", self.eyes)
        print("Его увлечение - ", self.hobby)

#    def getname(self):
#            print("Ваш друг ", self.name)
#    def getage(self):
#            print("Его возраст - ", self.age)
#    def getcity(self):
#            print("Он из города ", self.city)
#    def gethair(self):
#            print("Цвет его волос - ", self.hair)
#    def geteyes(self):
#            print("Цвет его глаз - ", self.eyes)
#    def gethobby(self):
#            print("Его увлечение - ", self.hobby)