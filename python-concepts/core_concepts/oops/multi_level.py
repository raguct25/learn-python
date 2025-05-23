# Mutli level inheritance same function name 

# if declared same it' overwrites functions

class GrandParent:
    def __init__(self):
        print("*** constructor GP ******")

    # def grand_parent(self):
    def test_func(self, **kwargs):
        print("Grandparent method called")
        return f"I am a Grand Parent class - mul {kwargs.get("val1")*kwargs.get("val2")}"


class Parent(GrandParent):

    def __init__(self):
        print("*** constructor P ******")
        super().__init__()

    # def parent_func(self):
    def test_func(self, n1,n2):
        print("Parent method called")
        # super().grand_parent()
        # super().test_func()
        result = super().test_func(val1=n1, val2=n2) # capture return values
        print("parent result ->", result)
        return f"I am a Parent class - sub {n1-n2}"

class Child(Parent):

    def __init__(self):
        print("*** constructor C ******")
        super().__init__()

    # def child_func(self):
    def test_func(self, *args):
        print("Child method called", args)
        n1, n2 = args
        # super().parent_func()
        # super().test_func()
        result = super().test_func(n1, n2) # capture return values
        print("child result -> ", result)
        return f"I am a child class add {n1+n2}"
    

c1 = Child()

print("object c1", c1)

print("object c1", c1.test_func)

print("object c1", c1.test_func(10,20))
