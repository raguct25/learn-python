from access_specifiers_functions import ParentAccessSpecifiers

class StrangerClass():

    def access_parent_class(self, class_object):

        print("\n ***** stranger func called ********** \n")
        print("Subclass public name", class_object.public_name)
        print("Subclass protected name", class_object._protected_name)
        # print("Subclass private name", class_object.__private_name) # it does not access private

        #if want access use name mangling
        print("Private variable ---> ", class_object._ParentAccessSpecifiers__private_name)

        class_object.public_class()
        class_object._protected_class()
        try:
            class_object._ParentAccessSpecifiers__private_class()
            class_object.__privateclass() # it wont work

        except Exception as e:
            print("error execute", e)


o1 = StrangerClass()
o2= ParentAccessSpecifiers()

# AttributeError: type object 'ParentAccessSpecifiers' has no attribute 'public_name'
# o1.access_parent_class(ParentAccessSpecifiers) # it won't access. if want access create object and pass an object

# it will works
# o1.access_parent_class(o2)

access_private = o1.access_parent_class(o2)

# It wont work
# access_private._ParentAccessSpecifiers__private_class() 
# # AttributeError: 'NoneType' object has no attribute '_ParentAccessSpecifiers__private_class'
