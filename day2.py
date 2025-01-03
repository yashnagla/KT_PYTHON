# While
# Q Write a program to print the first 10 Even numbers
num = 2
while (num <= 20):
    print(num)
    num += 2

# Q Write a program to print the first 10 Odd numbers
num = 1
while (num <= 20):
    print(num)
    num += 2

# Q Write a program to print the first 10 Natural numbers
num = 1
while (num <= 10):
    print(num)
    num += 1

# Q Write a program to print the first 10 Whole numbers
num = 0
while (num < 10):
    print(num)
    num += 1

# Q Write a program to print first 10 integers and their squares using while loop.
num = 1
while (num <= 10):
    print(num, num*num)
    num += 1

# Q Write for loop statement to print the following series: 10, 20, 30 ... ... 300
num = 10
while (num <= 300) :
    print(num)
    num += 10

# Q Write a while loop statement to print the following series 105, 98, 91 ... 7
num = 105
while num >= 7:
    print(num)
    num -= 7

# Q Write a program to print first 10 natural number in reverse order using while loop.
num = 10
while num > 0 :
    print(num)
    num -= 1

# Q Write a program to print table of a number entered from the user.
num = int(5)
i = 1
while i <= 10 :
    print(num*i)
    i += 1

# Q Write a program to print sum of first 10 Even numbers.
num = 2
sum = 0
while (num <= 20) :
    sum += num
    num += 2
print(sum)


# if-else
i = 20
if (i > 0):
    print(i,"is positive")
else:
    print("i is 0 or Negative")


age = 25
experience = 10
if age > 23 and experience > 8:
    print("Eligible.")
else:
    print("Not eligible.")


i = 10
if (i == 10):
    if (i < 15):
        print(i ,"is smaller than 15")
    if (i < 12):
        print(i ,"is smaller than 12 too")
    else:
        print(i ,"is greater than 15")
else:
    print("i is not equal to 10")


i = 25
if (i == 10):
    print(i ,"is 10")
elif (i == 15):
    print(i ,"is 15")
elif (i == 20):
    print(i ,"is 20")
else:
    print(i ,"is not present")


# Q Write a program to check whether a number entered by user is even or odd.
num = int(input("Enter a number :- "))
if (num % 2 == 0):
    print("Even")
else:
    print("Odd")

# Q Write a program to check whether a number is divisible by 7 or not.
num = int(input("Enter a number :- "))
if (num % 7 == 0):
    print(num, "is divisible to 7.")
else:
    print("Not a valid number.")

# Q. Write a program to Isp ay "Hello" 1 a num er entere of five, otherwise print "Bye".
num = int(input("Enter a number :- "))
if (num % 5 == 0):
    print("Hello")
else:
    print("Buy")


# Q Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
num = int(input("Enter a number :- "))
divisible = num % 3
if (divisible == 3):
    print("Last digit is 3")
else:
    print("Last digit is not 3")



# Function
# Q Write a user defined function to find the area of rectangle.
def rect(a,b) :
    print(a*b)
rect(5,6)

# Write a user defined function to print "Python Fundamentals" five times.
def str(a) :
    print(a * 5)
str("Hello")

# Write a user defined function to find the volume of cube.
def cube(a) :
    print(a*a*a)
cube(5)

# Q WAF to print the length of a list. ( list is the parameter)
list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = [1,8,9,0]
def listLength(a):
    print(len(a))
listLength(list1)
listLength(list2)

# Q2 WAF to print the elements of a list in a single line. ( list is the parameter)
list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = [1,8,9,0]
def listElement(a):
    for val in a:
        print(val, end=" ")
listElement(list1)
listElement(list2)

# Q WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
num = int(input("Enter number to find factorial :- "))
cal_fact(num)
cal_fact(int(input("Enter number to find factorial :- ")))


# Q WAF to convert USD to INR.
def converter(usd_val):
    print(usd_val, "USD =",usd_val * 85, "INR")
converter(100)

# Q WAF to print even ot odd based on input
def num(y):
    if (y % 2 == 0) :
        print("Even")
    else:
        print("Odd")

num1 = int(input("Enter number and see weather it is a even or odd :- "))
num(num1)

# for-loop
# Q. Write program to print the following pattern.
# 1
# 12
# 123
# 1234
for i in range(1, 5+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


# Q Write program to print the following pattern.
# *****
# ****
# ***
# **
# *
for i in range(5+1, 1, -1):
    for j in range(i-1):
        print("*", end=" ")
    print()

# Q Accept 10 numbers from the user and display their average.
responses = [input(f"Enter input {i + 1}: ") for i in range(10)]
sum = 0
for i in range(10):
    num = int(input("Enter number :- "))
    sum += num
print("Average of 10 entered numbers is :- ", sum/(i+1))

# Q Write a program to print all prime numbers that fall between two numbers including both(accept two numbers from the user)
a = int(input("Enter the starting number :- "))
b = int(input("Enter the ending number :- "))
for num in range(a, b + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")