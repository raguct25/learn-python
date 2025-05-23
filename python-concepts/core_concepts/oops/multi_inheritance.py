# Inheritance

# class InheritanceClass(TestClassParent, TestClass):
#     def __init__(self, name, age, loc, mob, **kwargs):
#         print("*** InheritanceClass called ***")
#         # super().__init__(name, age, loc, mob) #if want access parent class must call Parent class constructor for access - use by super()
#         # super().__init__(loc, mob)
 
#         # super().__init__(name=name, age=age, loc=loc, mob=mob)
#         super().__init__(name, age, loc,mob, kwargs)



# t1 = InheritanceClass("ragugandhi", 20, "coimbatore", 9500301052, val1=50, val2=45) # when we create object . it will execute construtor 

# Aceess multi class

from test_class import ParentA, ParentB


class InheritanceClass(ParentA, ParentB):
    def __init__(self, name, age, location):
        print("Child init called")
        self.location = location
        super().__init__(name=name, ag=age)

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")

c = InheritanceClass("Ragu", 30, "Coimbatore")
c.greet()
c.show_age()
c.show_info()




