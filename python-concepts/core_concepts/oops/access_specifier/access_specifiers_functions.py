class ParentAccessSpecifiers():

    def __init__(self):
        print("initial called")
        self.public_name = "I am Public"
        self._protected_name = " I am Protected"
        self.__private_name = " I am Private"

    def public_class(self):
        print("\n ------- PUBLIC -------- \n")
        print("public name", self.public_name)
        print("protected name", self._protected_name)
        print("private name", self.__private_name)
    
    def _protected_class(self):
        print("\n ------- PROTECTED -------- \n")
        print("public name", self.public_name)
        print("protected name", self._protected_name)
        print("private name", self.__private_name)

    def __private_class(self):
        print("\n ------- PRIVATE -------- \n")
        print("public name", self.public_name)
        print("protected name", self._protected_name)
        print("private name", self.__private_name)

    def access_sameclass(self):
        print("\n ------- Same calls access sepecifiers function -------- \n")
        self.public_class()
        self._protected_class()
        self.__private_class()


# Single inheritance

class ChildAccessSpecifier(ParentAccessSpecifiers):

    def access_subclass(self):
        print("\n ------- Child calls access sepecifiers -------- \n")
        print("Subclass public name", self.public_name)
        print("Subclass protected name", self._protected_name)
        # print("Subclass private name", self.__private_name) # it's a private varible it won't access in subclass
        # AttributeError: 'ChildAccessSpecifier' object has no attribute '_ChildAccessSpecifier__private_name'. Did you mean: '_ParentAccessSpecifiers__private_name'?
        self.public_class()
        self._protected_class()
        # self.__private_class() # it won't work it's private functions
        # self._ParentAccessSpecifiers__private_class() # it can access
        try:
            print("Subclass private name", self.__private_name)
            # self.__private_class()
        except AttributeError as e:
            print("Error", e)




# o1 = ParentAccessSpecifiers()
# o1.access_sameclass()

# o1.public_class()
# o1._protected_class()

# o1.__private_class() # it won't access directly AttributeError: 'ParentAccessSpecifiers' object has no attribute '__private_class'

# it works
# o1._ParentAccessSpecifiers__private_class() # can access private method

# o2 = ChildAccessSpecifier()
# o2.access_subclass()