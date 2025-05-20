# Syntax error
# name = "error message

# def test_fun()
#     print("function missing :")
    
# print(name)

# test_fun()

# Runtime error

def divide_fun(a, b):    
    return (a/b)

print(divide_fun(10,5))

# error throws ZeroDivisionError: division by zero
# divide_fun(10,0)


numbers = [10,15,20,30]
# IndexError: list index out of range
# print (numbers[6])

#Logical Error
# here actully defined sum it will add two number. but we perform subtract two numbers

def sum(a, b):
    return a-b

logicalError = sum(20, 30)

print(logicalError)


# error handling

def division(n):
# ValueError: invalid literal for int() with base 10: 'test'
    # int("test")
    return 10/n

try:
    division(5)
    # division(0)

# Exception is common class it capture all types of errors

# except Exception as e:

except ZeroDivisionError as e:

    print("Error e ____-----____", e)
    print("the number 10 is not divide by 0")

except ValueError as e:
    print("the string value could not convert")

# if error not comes this block will call
else:
    print("No errors called so else will call")

# finally block will call fail or success
finally:
    print("The finally block will called")