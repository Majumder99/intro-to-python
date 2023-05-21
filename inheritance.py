class Mammal:
    def walk(self):
        print("walk")

# inferitance


class Dog(Mammal):
    def bark(self):
        print("barking")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
