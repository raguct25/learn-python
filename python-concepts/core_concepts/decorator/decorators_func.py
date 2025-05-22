# Decorator example


# this is normal way callble functions

def decorator_fun(callable_func):
    print("decorator_fun called") 
    # print("decorator_fun called", callable_func()) #  callable_func is <function addition at 0x79b79e726700>

    def decorator_fun_inner(): # Extends function and not run imediately
        print("decorator_fun_inner start")
        return_func = callable_func()
        print(f"callable functions is return {return_func}")
        print("decorator_fun_inner end")
    # decorator_fun_inner() # if want call can declare it
    return decorator_fun_inner # decorator_fun_inner is return

def addition():
    print("addtiion caalble function called")
    return 25 + 28

def subtraction():
    print("subtraction caalble function called")
    return 45 - 30

function_experssion = decorator_fun(addition) # this declartion has been executed initially . decorator_fun only will call it called  assignment statement or  assignment statement 

# print("function_experssion", function_experssion) # it stored decorator_fun_inner the output is <function decorator_fun.<locals>.decorator_fun_inner at 0x736c02c227a0>
function_experssion() # it execute decorator_fun_inner. the decorator_fun_inner will call argument function callable_func()


function_experssion = decorator_fun(subtraction) # this declartion has been executed initially . decorator_fun only will call it called  assignment statement or  assignment statement 

function_experssion() 


# decorator fucntion call using decorator syntax

print("\n ************ Decorator **************** \n")

print("\n ************ Addition callble fun **************** \n")


@decorator_fun
def addition():
    print("addtiion caalble function called")
    return 25 + 28

addition()

print("\n ************ subtraction callble fun **************** \n")


@decorator_fun
def subtraction():
    print("subtraction caalble function called")
    return 15 - 30

subtraction()