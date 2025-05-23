class ParentAccessSpecifiers():

    def __init__(self):
        print("initial called")
        self.public_name = "I am Public"
        self._protected_name = " I am Protected"
        self.__private_name = " I am Private"

    def access_sameclass(self):
        print("\n ------- the same calls access sepecifiers called -------- \n")
        print("public name", self.public_name)
        print("protected name", self._protected_name)
        print("private name", self.__private_name)


class ChildAccessSpecifier(ParentAccessSpecifiers):

    def access_subclass(self):
        print("\n ------- Child calls access sepecifiers called -------- \n")
        print("Subclass public name", self.public_name)
        print("Subclass protected name", self._protected_name)
        # print("Subclass private name", self.__private_name) # it's a private varible it won't access in subclass
        # AttributeError: 'ChildAccessSpecifier' object has no attribute '_ChildAccessSpecifier__private_name'. Did you mean: '_ParentAccessSpecifiers__private_name'?
        try:
            print("Subclass private name", self.__private_name)
        except AttributeError as e:
            print("Error", e)




o1 = ParentAccessSpecifiers()
o1.access_sameclass()

o2 = ChildAccessSpecifier()
o2.access_subclass()