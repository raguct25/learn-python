# Variables

"""
Variable names are case-senstive.
MYVAR and myvar is different
Don't use python keywords - ( eg: if, else, def, for, etc )
should be descriptive and meaningful name for easy to readble
use lowercase and snakecase for varible names
avoid using single character for varble except loop variables
The variable names should not start with numbers and underscores _ (if used underscores _ in python its specifi naming convention and it private variable so avoid _ also)
No need to define variables ( var, let, const ) in pythobn
"""

var1 = "ragu"

print("1st --> ", var1)
print("type --> ", type(var1))


var1 = 100

print("2nd --> ", var1)
print("type --> ", type(var1))


# 1var = "gandhi"  this declartion is encountered error

_var = "The underscore varibles"


print("3rd --> ", _var)
print("type --> ", type(_var))

_var_ = "The underscore varibles"

print("4th --> ", _var_)
print("type --> ", type(_var_))


myVar = "myVar case-senstive"
MYVAR = "MYVAR case-senstive"

format_string = f"Formatted string {var1}" # In JS string literals 

print("5th --> ", myVar)

print("6th --> ", MYVAR)

print("format_string --> ", format_string)