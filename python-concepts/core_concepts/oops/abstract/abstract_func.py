# Abstract class

from abc import ABC, abstractmethod

class TestAbstractClass(ABC):

    def __init__(self):
        print("The abstrct class main called")
        super().__init__()

    def info_get(self):
        print("I am a normal methods but am a abstrct class")

    @abstractmethod
    def get_info(self):
        # print("The abstrct methoid called") # it don't print here just declare method and pass it
        pass

# we can't create object here
# TypeError: Can't instantiate abstract class TestAbstractClass without an implementation for abstract method 'get_info'

# t2 = TestAbstractClass()