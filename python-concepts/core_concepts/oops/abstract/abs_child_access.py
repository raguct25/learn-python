from abstract_func import TestAbstractClass

class ChildClass(TestAbstractClass):

    def __init__(self):
        print("The child class has called")
        super().__init__()

    def get_info(self): # if not implement abstract class it won't work should implment TestAbstractClass all abstarct methods
        print("I am the abstract access class")


o1 = ChildClass()

o1.get_info()
o1.info_get()
