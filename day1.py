# Variables
#  Numeric Data Type
var1 = 1
var2 = True
var3 = 1.2362
var4 = 10+3j

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))


# String Data Type
str = "Hello World!"
print(type(str))
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + " Test")

# List Data Type
x = [['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]
y = [1,2,3,4,5,6]
print(x)
print(type(x))
print(x[0])
print(x[1:3])
print(x[2:])
print(x * 2)
print(x + y)

# Tuple Data Type
tup = ('abcd', 786 , 2.23, 'john', 70.2)
tup2 = (1,2,3,4,56,7,87)
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[2:])
print(tup * 2)
print(tup + tup2)

# Range Function
for i in range(5):
    print(i)
for i in range(2,5):
    print(i)
for i in range(1,5,2):
    print(i)

# Bytes Data Type
b1 = bytes([65, 66, 67, 68, 69, 90])  
print(b1)
b2 = b'Hello'  
print(b2)

# Bytearray Data Type
ba1 = bytearray([72, 101, 108, 108, 111])
print(ba1)

# Memoryview Data Type
dt = bytearray(b"Hello World!")
mv = memoryview(dt)
print(mv)

# Dictionary Data Type
dic = {1:'one', 2:'two', 3:'three'}
print(dic)
print(type(dic))
print(dic[1])
print(dic[2])
print(dic[3])
dic[3] = "updatedThree"
print(dic[3])
dic[4] = "Four"
print(dic)

# Set Data Type
st = {1,2,3,4,5,6,7,8,9,0}
print(st)
print(type(st))

# Boolean Data Type
f1 = 1
f2 = 3
print(bool(f1==f2))
print(bool(f1<=f2))
print(bool(f1>=f2))
a = ()
print(bool(a))
a = 0.0
print(bool(a))
a = 10
print(bool(a))

# None Type
x = None
print(x)
print(type(x))


# List
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append("orange")
print(fruits)

x = fruits.copy()
print(x)

print(fruits.count("banana"))

cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

print(fruits.index("apple"))
print(fruits.index("banana"))

fruits.insert(4,"Kiwi")
print(fruits)

print(fruits.pop(1))

fruits.remove("Kiwi")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(fruits.clear())



# Operators
# # Arithmetic Operators
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# # Comparison Operator
x = 50
y = 20
print(x == b)
print(x != b)
print(x >= b)
print(x <= b)
print(x > b)
print(x < b)

# # Assignment Operator
num = 10
num += 5
print(num)
num -= 5
print(num)
num *= 5
print(num)
num /= 5
print(num)
num %= 5
print(num)
num **= 5
print(num)

# Logical Operators

name = input("Enter Your Name :- ")
age = int(input("Enter your age :- "))
marks = float(input("Enter your marks :- "))

print("Your Name :- ", name)
print("Your Age :- ", age)
print("Your Marks :- ", marks)



# Strings
a = "Banana"
print(a)

b = '''Hi there,
How you do'ing.'''
print(b)

print(a.capitalize())
print(a.center(20))
print(a.find("e"))
print(a.index("n"))
print(a.lower())
print(a.islower())
print(a.upper())
print(a.isupper())
print(a.swapcase())



# TypeCasting
# Implicit Casting
a=True
b=10.5
c=a+b
print(c)

# Explicit Casting
a = int("110011", 2)
print(a)

a = int("20", 8)
print(a)

# Hexa-Decimal String to Integer
a = int("2A9", 16)
print(a)

a=[1,2,3,4,5]
b=(1,2,3,4,5)
c="Hello"

print(list(c))

print(tuple(c))

print(str(b))

result = complex(1, 5)
print(result)

integer_number = 111
print(hex(integer_number))

integer_number = 219
print(oct(integer_number))



# Variables
day = "Friday"
print(day)

month = 12
print(month)

year = 2024
print(year)

salary = 120000.546
print(salary)

bool = True
print(bool)