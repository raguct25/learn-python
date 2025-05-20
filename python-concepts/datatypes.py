#Datatypes

"""
The datatypes is calssify the data
The different datatypes require different amounts of memory to store
The datatypes are:
int - Integer values (5,6, -5, -6, 567)
float - Float values (4.33, 456.000 , -78.223, -56.000)
str - Represents unicode character inside the single quotes '' or double quotes ""
boolean -Boolean values ( True , False )
list -  [] - ordered collection of iterms and its mutable
tuple - () - ordered collection of iterms and its Immutable
dictionary - {} - collection of items key pair values  (don't allow duplicate keys, allow values)
set - {} - unorder collection of unique items (don't allow duplicate)
frozenset - same as set but it's Immutable
NoneType - Values is None - it represents absence of value or null value
"""

#examples

value = 25
amount = 55.55
name= "Ragu"
is_update = True
eg_list = [1, 2, "ragu", 55.00, True, False, ["test", "QA"]]
eg_tuple= (1, 2, "ragu", 55.00, True, False, ["test", "QA"])
eg_dict = {"name": "ragu", "age": 35, "hoppies": ["playing", "Travel"]}
# eg_set = {["test", "QA"], 0, 56, 78, 56, 44, 33, True, ["test", "QA"], False, eg_tuple} # inside list, dict, tuple doesn't allow here
eg_set = { 0, 56, 78, 56, 44, 33, True, False, is_update}

eg_none = None

print("value", value)
print("value", type(value))

print("amount", amount)
print("amount", type(amount))

print("name", name)
print("name",type( name))

print("is_update", is_update)
print("is_update",type( is_update))

print("eg_list", eg_list)
print("eg_list",type( eg_list))

print("eg_tuple", eg_tuple)
print("eg_tuple",type( eg_tuple))

print("eg_dict", eg_dict)
print("eg_dict",type( eg_dict))

print("eg_set", eg_set)
print("eg_set",type( eg_set))

print("eg_none", eg_none)
print("eg_none",type( eg_none))