class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        self.weight += 1

class Panda:
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.skill = skill
        self.name = name
        self.age = age
        self.__weight = weight

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name + " " + str(self.age)

    def eat(self):
        print("NOM NOM NOM")
        self.__weight += 10

    def _sleep(self):
        self.__weight += 10

    def __set_name(self):
        self.name = name

panda = Panda ("Ivan", 10, 200, 10)
panda.eat()
print(panda.weight)
