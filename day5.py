# Decorator
# Q1 Write a Python program to create a decorator that logs the arguments and return value of a function.
def decorator(func):
    def wrap(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrap
@decorator
def multi_num(x, y):
    return x*y
result = multi_num(10, 20)
print(result)


# Q2 Write a Python program to create a decorator function to measure the execution time of a function.
import time
def measureExecutionTime(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        executionTime = endTime - startTime
        print(f"Function {func.__name__} took {executionTime:.4f} seconds to execute.")
        return result
    return wrapper
@measureExecutionTime
def calMulti(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot
result = calMulti([1,2,3,4,5])
print(result)


# Q3 Write a Python program to create a decorator to convert the return value of a function to a specified data type.
def convertDataType(dataType):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return dataType(result)
        return wrapper
    return decorator
@convertDataType(int)
def addNum(x, y):
    return x+y
result = addNum(10, 20)
print(result, type(result))


# Q4 Write a Python program that implements a decorator to cache the result of a function.
def cacheResult(func):
    cache = {}
    def warpper(*arge, **kwargs):
        key = (*arge, *kwargs.items())
        if key in cache:
            print('...........')
            return cache[key]
        result = func(*arge, **kwargs)
        cache[key] = result
        print(',,,,,,,,,,,,,,,,,')
        return result
    return warpper
@cacheResult
def calMul(x, y):
    return x*y
print(calMul(4, 5))
print(calMul(4, 5))
print(calMul(5, 5))
print(calMul(4, 5))
print(calMul(5, 5))
print(calMul(-3, 7))


# Q5 Write a Python program that implements a decorator to validate function arguments based on a given condition.
def cacheCube(condition):
    def decorator(func):
        def warpper(*arge, **kwargs):
            if condition(*arge, **kwargs):
                print("........")
                return func(*arge, **kwargs)
            else:
                raise ValueError("Invalid")
        return warpper
    return decorator
@cacheCube(lambda x : x > 0)
def calCubs(x):
    print(":::::::::::::")
    return x ** 3
print(calCubs(3))
print(calCubs(3))
print(calCubs(5))
print(calCubs(9))



# Generator
# A generator function that yields 1 for first time,2 second time and 3 third time, to print the next value
def fun():
    yield 1
    yield 2
    yield 3
for val in fun():
    print(val)

# Q1 Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.
n = int(input("Enter a number to find cube of :- "))
def cubGen(n):
    for i in range(1, n+1):
        yield i**3
cubes = cubGen(n)
print(cubes)
for num in cubes:
    print(num)

# Q2 Write a Python program to implement a generator that generates random numbers within a given range.
import random

start = int(input("Enter range start point :- "))
end = int(input("Enter range end point :- "))

def ranRange(start,end):
    while True:
        yield random.randint(start,end)
ranNum = ranRange(start,end)
for i in range(10):
    print(next(ranNum))

# Q3 Write a Python program that creates a generator function that generates all prime numbers between two given numbers.
n = int(input("Enter the number of prime number you want to print :- "))
def isPriNum(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def primeNumGenerator():
    n = 2
    while True:
        if isPriNum(n):
            yield n
        n += 1
primes = primeNumGenerator()
print(n)
for i in range(n):
    print(next(primes))

# Q4 Write a Python program to implement a generator function that generates the Fibonacci sequence.
def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

n = int(input("Enter the number of fibonacci number you want to print :- "))

print(n)

fib = fibonacci()
for i in range(n):
    print(next(fib),end=" ")

# Q5 Write a Python program to implement a generator function that generates all permutations of a given list of elements.
def listPermutation(ele):
    if len(ele) <= 1:
        yield ele
    else:
        for p in listPermutation(ele[1:]):
            for i in range(len(ele)):
                yield p[:i] + ele[0:1] + p[i:]
nums = [1, 2, 3]
print(nums)
for p in listPermutation(nums):
    print(p)

# Q6 Write a Python program to implement a generator that yields all possible combinations of a given list of elements.
def listCom(ele, r):
    if r == 0:
        yield []
    elif r > len(ele):
        return
    else:
        for i in range(len(ele)):
            currEle = ele[i]
            remEle = ele[i+1:]
            for combi in listCom(remEle, r-1):
                yield [currEle] + combi
nums = [1,2,3,4]
print(nums)

r = int(input("Input length of each combination :- "))

for comb in listCom(nums, r):
    print(comb)