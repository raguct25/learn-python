# Inheritance

from class_object import TestClass # if i called this class. I have created object there so when i inheritance this calss the all objects will executed

# access single  class

class InheritanceClass(TestClass):
        
    def __init__(self, name, age, *args, **kwargs):
        super().__init__(name, age, *args, **kwargs)
    # def __init__(self, name, age):
        print("*** InheritanceClass called ***")
        # super().__init__(name, age, args, kwargs) #if want access parent class must call Parent class constructor for access - use by super()
    

t1 = InheritanceClass("ragugandhi", 20, "coimbatore", 9500301052, val1=50, val2=45) # when we create object . it will execute construtor 
# t1 = InheritanceClass("ragugandhi", 20, "coimbatore", 9500301052)



print(t1.display_info())

print("\n ------------ access from parent -------------- \n")
print("child class access name", t1.name)
print("child class access name", t1.age)
print("child class access name", t1.loc)
print("child class access name", t1.mob)



