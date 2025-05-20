# match statement examples

# value checking
def value_match_statement(val):
    match val:
        case 10:
            print("the 10 is matched")
        case "test":
            print("test value is matched")
        case _:
            print("the deafult case")


value_match_statement("test")
value_match_statement(10)
value_match_statement(100)


# type checking

def type_match_statement(val):
    print("val", val)
    match val:
        case bool(): # if check bool type the case should declare before int() case
            print("TYPE boolean called")
        case int():
            print("TYPE Integer called")
        case str():
            print("TYPE String called")
        case float():
            print("TYPE float callled")
        # case bool():
        #     print("TYPE tboolean called")
        case _:
            print("TYPE the deafult case")

type_match_statement(10)
type_match_statement("ragu testing")
type_match_statement(10.45)
type_match_statement(True)
type_match_statement(None)


# structure checking

def structure_match_statement(val):
    match val:
        case [10, 25]:
            print("the 10 is matched")
        case [s, r]:
            print(f"The list values is {s} and {r}")
        case {"name": ragu, "age": 35}:
            print("The dict values is called")
        case _:
            print("the deafult case")

structure_match_statement([10, 25])
structure_match_statement([100]) # default case
structure_match_statement([101, 90])
structure_match_statement({"name": "ragu", "age": 3}) # default case values is incorrect
structure_match_statement({"name": "ragu", "age": 35})



# guards - condition checking

def condition_match_statement(val):
    match val:
        case val if val == 10:
            print(f"TYPE Integer called {val} is 10 correct")
        case val if val != "ragu":
            print("TYPE String called")
        
        case _:
            print("TYPE the deafult case")

condition_match_statement("ragu testing")
condition_match_statement(10)
