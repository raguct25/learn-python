#  Functions examples

from functools import reduce

# Nested functions

def nested_func():
    print("I am nested function")

    def inside_func():
        print("I am inside_func")

    def inside_second_func():
         print("I am inside_second_func")
        
    inside_func() # if not call it could not trigger
    inside_second_func() # if not call it could not trigger


nested_func()

print("\n********** Returning ************\n")

# Returning functions

def return_func():
    print("I am next function")

    def testfun(): # this won't call latets  testfun() will call
        print("inner first fucntions called")
   
    def inside_func():
        print("I am inside_func")
        # return "Success inside functions" # TypeError: 'str' object is not callable
        return testfun
        # return 15 + 20 #TypeError: 'int' object is not callable

    # return "Success inside functions" # TypeError: 'str' object is not callable and this return is return_func  

        # return inside_func # if define inner fucntion return it will throws errro test_return_func() TypeError: 'NoneType' object is not callable

    def testfun():
        print("inner second fucntions called")

    return inside_func


# return_func() # this not get returning functions. if want wd can use assigmennt statement

test_return_func = return_func()
test_return_func()

inner_fun = test_return_func()
inner_fun()

print("\n***** Closures functions ******\n")

# Closure functions

def closures_func(arg):
    print("I am Closures function")
    name="Outer closure funtion variables"
    print(f"{name}")

    def innner_closures():
        print("I am a inner closures functions")
        print(f"I am a {name}")
        print(f"I am a {arg}")
        # name = "Inner closure funtion variables" # UnboundLocalError: cannot access local variable 'name' where it is not associated with a value
    # name = "Inner closure funtion variables" # the outer function varible has been overwrite
    
    def innner_closures_second():
        print("innner_closures_second functions")

    # return (innner_closures, innner_closures_second) # it could not retrurn . TypeError: 'tuple' object is not callable
    return innner_closures


# closures_func()
# test_closure = closures_func() # variable access by without arguments
test_closure = closures_func("pass as arguments") # variable access by arguments
del closures_func # it could be delete but the reference test_closure will storing the return funtions so it execute next line
# del closures_func() # it can't delte . SyntaxError: cannot delete function call
test_closure()


print("\n ******** Functions store as data structure ***********\n")


def add_fun(n1, n2): 
    return n1+n2

def sub_fun(n1, n2):
    return n1 - n2

dict_func = {
    "add": add_fun(25,28), # the arguments called as positional aruguments
    # "sub": sub_fun() # TypeError: sub_fun() missing 2 required positional arguments: 'n1' and 'n2'. 
    "sub": sub_fun
}

# without pass args
print(dict_func["add"])
# print(dict_func["sub"])

#pass args
# print(dict_func["add"](45,55))
print(dict_func["sub"](45,55))

print("\n ******** Functions pass as arguments ***********\n")

def pass_args_func(call_fun, n1, n2):
    return call_fun(n1, n2)


pass_args_func_add = pass_args_func(add_fun, 25,28)
pass_args_func_sub = pass_args_func(sub_fun, 5,28)

print(pass_args_func_add)
print(pass_args_func_sub)


print("\n ******** *args and **kwargs ***********\n")

# using args

# def test_add_fun(args): # its a single args but we pass multiple, if pass multiple args the functions args will expand its handle to complicate
def test_add_fun_args(*ragu): # avoid multiple args use *args
    a, b, c, d, e = ragu

    print("args sum", a+b+c+d+e)

    sum = 0
    for number in ragu:
        sum +=number
    print("total sum", sum)

#test_add_fun_args(45, 3, 4, 5) # ValueError: not enough values to unpack (expected 5, got 4)

test_add_fun_args(45, 3, 4, 5, 10)

# using kwargs

def test_add_fun_kwargs(*args, **ragu):
    # {n1, n2} = ragu # destructure won't works

    n1, n2 = args

    total_sum = ragu.get("n1") + ragu.get("n2")
    print("args sum", ragu.items())
    print("total_sum",total_sum)

    sum = 0
    for valuet, keyt in ragu.items(): # loop varible or iteration varible valuet, keyt the first declartion is key , second is value
        print("key", keyt)
        print("value", valuet)
        sum +=keyt
    print("Iterate total sum", sum)

    add_args_kwargs = n1+ n2 + ragu.get("n1")
    print("add_args_kwargs", add_args_kwargs)
    print("add_args", n1+ n2)


# we pass both arguments *args and **kwargs
test_add_fun_kwargs(25, 25, n1=15, n2=25)


print("\n ******** Lambda functions ***********\n")

# lambda fucntions pass arguments

add = lambda a, b : a +b

# print("add", add)  # <function <lambda> at 0x7a46c898eca0>

print(add(25,30))

# using map lambda - return update values

names = ["ragu", "gandhi", "daniel"]

map_lambda = list(map(lambda name : name.upper(), names))

# if used name.upper without parenthesis # [<built-in method upper of str object at 0x782a5e918810>, <built-in method upper of str object at 0x782a5e919950>, <built-in method upper of str object at 0x782a5e9199b0>]
print("map_lambda", map_lambda)

# using filter lambda - return filtered values

nums = [11, 22, 33, 44, 55, 66, 77, 88]

filter_lambda = list(filter(lambda x: x % 2 == 0, nums))

print(filter_lambda)

# using reduce lambda - return single value
# should import reduce from functools import reduce

numbers = [11, 22, 33, 44, 55, 66, 77, 88]

#first iterate [33, 33, 44, 55, 66, 77, 88]
#second iterate [66, 44, 55, 66, 77, 88] finally 396


reduce_lambda = reduce(lambda a,b: a+b, numbers)

print(reduce_lambda)

# reduce action is return single value

num_test = [45, 23, 12, 65, 55, 22, 78, 43, 95]

find_min = reduce(lambda a,b : a if a < b else b, num_test)

find_max = reduce(lambda a,b : a if a > b else b, num_test)

print(find_min)
print(find_max)