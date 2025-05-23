
# different classes have same name methods

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"


# create obeject for diffent object

dog = Dog()
cat = Cat()
cow = Cow()


# single function received different objects as parameter

def animal_sound(animal):
    print(animal.speak()) # the method name as same in all classes

# single function pass differnt objects

animal_sound(dog)
animal_sound(cat)
animal_sound(cow) 


# inheritance


# That print() is executed immediately when the class is being defined — not when an object is created.

# class DogClass():
#     print("_____DogClass______") # imdeiltely called
#     def __init__(self):
#         print("DogClass called")
#     def speak(self):
#         return "Woof!"
    
class Animal:
    print("_____Animal class called______") # imdeiltely called
    def __init__(self):
        print("Animal class called")
    def speak(self):
        return "Some sound"
    
class DogClass(Animal):
    print("_____DogClass______") # imdeiltely called
    def __init__(self):
        print("DogClass called")
    def speak(self):
        return "Woof!"



class CatClass(Animal):
    print("_____CatClass______") # imdeiltely called
    def __init__(self):
        print("CatClass called")

    def speak(self):
        return "Meow!"

# o1 = CatClass() # this constructor only called

animals = [DogClass(), CatClass(), Animal()]

for a in animals:
    print(a.speak())


