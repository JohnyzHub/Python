class Animal:
    no_of_animals = 0

    def __init__(self, name="Animal", color="Transparent", sound="Hmmm"):
        self.name = name
        self.color = color
        self.sound = sound
        Animal.no_of_animals += 1

    def run(self):
        print("{} is running.".format(self.name))

    def makeSound(self):
        print("{} is making {} sound.".format(self.name, self.sound))

    @staticmethod
    def getAnimalCount():
        return "Number of animals are {}".format(Animal.no_of_animals)

    def __str__(self):
        return "{} name is {}, it is {} in color and makes {} sound" \
            .format(self.__class__.__name__, self.name, self.color, self.sound)


class Dog(Animal):
    def __init__(self, name="Tommy", color="Black", sound="woof"):
        super().__init__(name, color, sound)

    def run(self):
        super(Dog, self).run()

    def makeSound(self, sound="kewww"):
        super().makeSound()
        print("{} is making {} sound.".format(self.name, self.sound))
        print("{} is making {} sound.".format(self.name, sound))


class Cat(Animal):
    def __init__(self, name="Beety", color="White", sound="Meow"):
        Animal.__init__(self, name, color, sound)


def main():
    dog = Dog()
    print(dog)
    dog.makeSound()
    dog.run()
    cat = Cat()
    print(cat)
    cat.makeSound()

    print(Animal.getAnimalCount())


main()
