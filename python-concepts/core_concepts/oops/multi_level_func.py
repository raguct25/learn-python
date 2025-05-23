# Mutli level inheritance differt function name

class GrandParent:
    def __init__(self):
        print("*** constructor GP ******")

    def grand_parent(self):
        print("Grandparent method called")
        return "I am a Grand Parent class"


class Parent(GrandParent):

    def __init__(self):
        print("*** constructor P ******")
        super().__init__()

    def parent_func(self):
        print("Parent method called")
        # super().grand_parent()
        result = super().grand_parent() # capture return values
        print("parent result ->", result)
        return "I am a Parent class"

class Child(Parent):

    def __init__(self):
        print("*** constructor C ******")
        super().__init__()

    def child_func(self):
        print("Child method called")
        # super().parent_func()
        result = super().parent_func() # capture return values
        print("child result -> ", result)
        return "I am a child class"
    

c1 = Child()

print("object c1", c1)

# print("object c1", c1.child_func)

# print("object c1", c1.child_func())
