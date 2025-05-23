# OOPS

# class creation

class TestClass:
    class_property = "class variable"
    print("initial---", class_property) # can access
    def __init__(self, name, age, *args, **kwargs): # create constructor must define self keyword and can pass attributes
        print("**** TestClass *****")
        print("**** name *****", name)
        print("**** age *****", age)
        print("**** args *****", args)
        print("**** kwargs *****", kwargs)

        # super().__init__(*args, **kwargs) # if used single inheritance no need declare super()
        self.name = name # if not defined - AttributeError: 'TestClass' object has no attribute 'name'
        self.age = age
        loc, mob = args
        self.loc = loc
        self.mob = mob
        print("self", self) #  <__main__.TestClass object at 0x74fcf358bc50>
        # print(class_property) # could not access class property if want access use self key
        print("constructor name", name)
        print("constructor age", age)

    def display_info(self):
        # print(class_property) # could not access class properties, if want access use self key
        print("class varible get ---> ", self.class_property) # can access class varibles by class or self
        # self is must. we can't process without self
        return f"from: {self.class_property} name is : {self.name}, age is : {self.age} , location is : {self.loc}, mobile no is: {self.mob}"



# t1 = TestClass("ragu", 25) # when the object is create immediately called constructor ( __init__ function will call )

# print("Access by object", t1.name)
# print("Access by object", t1.age)

# modify class variable

# t1.class_property = "Object variable" # not recommended update class variables

# print("t1", t1) # <__main__.TestClass object at 0x7df827f5b860>
# t1.display_info
# print(t1.display_info) # <bound method TestClass.display_info of <__main__.TestClass object at 0x7cc23fffb890>>

# print(t1.display_info())

# t2 = TestClass("gandhi", 35)

# print("Access by object", t2.name)
# print("Access by object", t2.age)


# print(t2.display_info())