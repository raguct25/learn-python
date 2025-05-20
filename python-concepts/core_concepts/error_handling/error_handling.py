# Error Handling

"""
Types of errors:

    * Syntax error
    * Runtime error
    * Logical error

Syntax Error:

    - It occurs when the code violates python syntax rules
    - It will parsing code and check line by line , if synntax has missing
    - Tht python is interpreter so it's detect before execution
    - If we used IDE's , error shows when we write a code
    - This can we find in terminal .the expected and errors will throws


Runtime Error:

    - It occurs while running the application
    - Sample inbuilt run time errors:
         
        * ZeroDivisionError - division b zero
        * ValueError - invalid type conversion
        * IndexError - trying non-existent index error - List
        * KeyError -  trying non-existent key error - dict
        * TypeError - incompatible data type
        * FileNotFoundError - trying non-existent file error

Logical Error:

    - It occurs when the programs execute without crashing but the output is incorrect or unexpected results
    - It could not throw error message
    - The error comes from our logical mistake

Error handling types:

    Try , except , else , Finally

    try - try block is define logic and functions
    except - if try block get error the except block will call
    else - if could not capture error the else block will call - If want run next functions the else can help
    Finally - the finally block will whatever success or fail finally block will call

"""