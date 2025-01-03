# Q1 Print the Sum of a Current Number and a Previous number
currentNumber = 0
previousNumber = 0
sum = 0
for i in range(0, 10):
    print("currentNumber :-", currentNumber, "previousNumber :-", previousNumber, "Sum :-", sum)
    previousNumber = currentNumber
    currentNumber += 1
    sum = currentNumber + previousNumber


# Q2 Write a Python code to accept a string from the user and display characters present at an even index number.
strs = input("Enter a string :- ")
for i in range(0, len(strs)-1, 2):
    print(i, strs[i])

# Q3 Write a Python code to remove characters from a string from 0 to n and return a new string.
str1 = input("Enter a string :- ")
x = int(input("Enter the index value from where you want to remove characters :-"))
str2 = str1[x:]
print(str2)


# Q4 Check if the first and last numbers of a list are the same
x = [1,2,3,4,5,6,7,8,2,1]
if x[0] == x[-1]:
    print("True")
else:
    print("False")

# Q5 Write a Python code to display numbers from a list divisible by 5
list1 = [10,20,33,46,55]
list2 = []
for i in list1:
    if i % 5 == 0:
        list2.append(i)
print(list2)

# Q6 Find the number of occurrences of a substring in a string
str = input("Enter a string :- ")
x = input("Enter the string you want to find :-")
print(str.count(x))

# Q7 Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
y = 1
x = int(input("Enter the ending point of the pattern :- "))
for i in range(y, x+1, 1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()


# Q8 Check Palindrome Number
x = input("Enter a number to check palindrom or not :- ")
y = x[::-1]
if x == y :
    print("True it's a palindrome")
else:
    print("It's not a palindrome")


# Q9 Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
firstList = [10, 20, 25, 30, 35]
secondList = [40, 45, 60, 75, 90]
rList = []
for i in firstList:
    if i % 2 == 0:
        rList.append(i)
for j in secondList:
    if j % 2 == 0:
        rList.append(j)
print(rList)


# Q10 Get each digit from a number in the reverse order.
numb = int(input("Enter a number to find reverse of it :- "))
reNumb = " ".join(reversed(str(numb)))
print(reNumb)


# Q11 Print multiplication table from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
    print()


# Q11 Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	        0
# Next $10,000	        10
# The remaining	        20
income = int(input("Enter your salary :- "))
taxableAmount = 0
if income <= 10000:
    taxableAmount = 0
elif income <= 20000:
    x = income - 10000
    taxableAmount = x * 10 / 100
else:
    taxableAmount = 0
    taxableAmount = 10000 * 10 / 100
    taxableAmount += (income - 20000) * 20 / 100
print(taxableAmount)


# Q12 Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *
x = int(input("Enter range :- "))
for i in range(x+1,1,-1):
    for j in range(1,i):
        print("*", end=" ")
    print()


# Q13 WAP to change the 2nd apperance of 'g' in 'google'.
text = "google"
listG = list(text)
print(listG)
count = 0
for i in range(len(listG)):
    if listG[i] == 'g':
        count += 1
        if count == 2:
            listG[i] = 'x'
print(listG)