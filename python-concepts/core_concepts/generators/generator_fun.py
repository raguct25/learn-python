# Generators

import sys

# yield example

def samplfun(x):
    print(f"sample function callled - {x}")
    return f"success yield {x}"


# samplfun()


def gen_test_fun():
    samplfun("first")
    print("genartor function called")
    yield print("Hi daniel") # it runs first call only next(). function could not run if has second yield the samplefun will call otherwise don't call
    # yield samplfun() 
    # samplfun()
    yield print("Hi Ragu")


runFun = gen_test_fun()


print(runFun) # <generator object gen_test_fun at 0x78eb48908a00>
next(runFun) # it will execute first yield only
# list(runFun) # reterive all yield functions
# print(next(runFun))
# print(next(runFun))

# () Parenthesis example

getItems = (num for num in range(1, 10))

print(next(getItems))
print(list(getItems))



# memory efficiiency

normalList = [num for num in range(1 , 10000000)]
genList = (num for num in range(1 , 10000000))

# print(normalList)
# print(next(genList))


print("size normal", sys.getsizeof(normalList))
print("gen normal", sys.getsizeof(genList))

# size normal 89095160 kB
# gen normal 192 KB

def yield_func():
    yield samplfun(1)
    yield samplfun(2)

test_yield_fun = yield_func()

def testFun():
    print("test fun called")
    try: 
        # print(list(test_yield_fun))  # all yield will execute and it will return [ val1, val2 ]
        print(next(test_yield_fun)) # one by one
        print(next(test_yield_fun))
        print(next(test_yield_fun)) # the yield declared two times but here iterate 3 times so it occurs StopIteration error we can handle except

    except StopIteration as e:
        print("throw exceptions no itreate called")
        
    finally:
        print("the yield function executed successfully")

testFun()