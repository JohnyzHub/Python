class Dog:
    def __init__(self, name="Tommy", color="Spots", sound="woof"):
        self.name = name
        self.color = color
        self.sound = sound

    def bark(self):
        print("{} is barking.".format(self.name))

    def run(self):
        print("{} is running.".format(self.name))

    def makeSound(self, sound="kewww"):
        print("{} is making {} sound.".format(self.name, self.sound))
        print("{} is making {} sound.".format(self.name, sound))


class Cat:
    def __init__(self, name="beety", sound="meow"):
        self.name = name
        self.sound = sound

    def eat(self):
        print("{} is eating.".format(self.name))

    def makeSound(self, sound="kewww"):
        print("{} is making {} sound.".format(self.name, self.sound))
        print("{} is making {} sound.".format(self.name, sound))


def main():
    dog = Dog()
    dog.bark()
    dog.makeSound()
    dog.run()
    """
    This doesn't work because the name if the parameter(colr)
    and the function(color()) are same.

    spotted.color()
    """
    cat = Cat()
    cat.eat()
    cat.makeSound()


main()
