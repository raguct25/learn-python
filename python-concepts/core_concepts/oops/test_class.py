# class TestClassParent:
#     def __init__(self, loc, mob, *args, **kwargs):
#     # def __init__(self, loc, mob, *args, **kwargs):

#         print("\n ---- TestClassParent -----\n")
#         super().__init__(*args, **kwargs)
#         # super().__init__(*args)
#         # loc, mob = args # won't work
#         self.loc = loc
#         self.mob =mob
#         print("constructor loc", loc)
#         print("constructor mob", mob)

        
class ParentA:
    def __init__(self, name, *args, **kwargs):
        print("ParentA init called")
        print("name", name)
        print("args", args)
        print("kwargs", kwargs)
       
        self.name = name
        super().__init__(*args, **kwargs)

    def greet(self):
        print(f"Hello from ParentA, Name: {self.name}")

class ParentB:
    
    def __init__(self, ag, *args, **kwargs):
        print("ParentB init called")
        print("age", ag)
        print("args", args)
        print("kwargs", kwargs)
        self.age = ag
        super().__init__(*args, **kwargs)

    def show_age(self):
        print(f"Age from ParentB: {self.age}")