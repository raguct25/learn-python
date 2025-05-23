from access_specifiers_variable import ParentAccessSpecifiers

class StrangerClass():

    def access_parent_class(self, class_object):

        print("\n ***** stranger func called ********** \n")

        print("Subclass public name", class_object.public_name)
        print("Subclass protected name", class_object._protected_name)
        # print("Subclass private name", class_object.__private_name) # it does not access private

        #if want access use name mangling
        print("Private variable ---> ", class_object._ParentAccessSpecifiers__private_name)




o1 = StrangerClass()
o2= ParentAccessSpecifiers()

# AttributeError: type object 'ParentAccessSpecifiers' has no attribute 'public_name'
# o1.access_parent_class(ParentAccessSpecifiers) # it won't access. if want access create object and pass an object

# it will works
o1.access_parent_class(o2)
