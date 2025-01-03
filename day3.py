# Classes and Object
# Q Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
b6e = Vehicle(240, 20)
# print(b6e.max_speed, b6e.mileage)


# Q Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self, brand):
        self.brand = brand
schoolBus = Bus("Volvo")
print(schoolBus.brand, b6e.max_speed, b6e.mileage)


# Q  Find a pair of elements from a given array whose sum equals a specific target number
class Find_Equals :
    def twoSum(self, nums, target) :
        lookup = {}
        for i, num in enumerate(nums) :
            if target - num in lookup :
                return (lookup[target - num], i)
            lookup[num] = i
print(Find_Equals().twoSum((10,20,30,40,50,60,70,80,90),110))


# Q Write a Python program to get all possible unique subsets from a set of distinct integers.
class SubSet:
    def subSets(self, sset) :
        return self.subsetsRecur([], sorted(sset))
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
print(SubSet().subSets([4,5,6]))


# Q Write a Python class to find the three elements that sum to zero from a set (array) of n real numbers.
class SumOfThreeFromSet:
    def threeSum(self, nums) :
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2 :
            j, k = i + 1, len(nums) - 1
            while j < k :
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
print(SumOfThreeFromSet().threeSum([-25,-10,-7,-3,2,4,8,10]))


# Q Write a Python class to implement pow(x, n).
class FindPower:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.pow(x,-n)
        val = self.pow(x, n//2)
        if n % 2 == 0:
            return val ** 2
        return val * val * x
print(FindPower().pow(2,-3))
print(FindPower().pow(3,5))
print(FindPower().pow(100,0))



# Q Write a Python class to reverse a string word by word.
class WordByWord:
    def revString(self, s):
        return ' '.join(reversed(s.split()))
print(WordByWord().revString('yash nagla'))


# Q Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
class InOutStr():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input()
    def printStr(self):
        print(self.str1.upper())

str1 = InOutStr()
str1.get_string()
str1.printStr()


# Q Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.
class AreaRect():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def reactangelArea(self):
        return self.length * self.width
newRect = AreaRect(5, 6)
print(newRect.reactangelArea())


# Q Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.
class Cir():
    def __init__(self,r):
        self.radius = r
    def cirArea(self):
        return self.radius ** 2 * 3.14
    def paraCir(self):
        return 2 * self.radius * 3.14
NewCir = Cir(8)
print(NewCir.cirArea())
print(NewCir.paraCir())



# Lambda
# Q WAP to print the square of a user input number using lambda
x = int(input("Enter a number to find the square :- "))
sq = lambda x : x ** 2
print(sq(x))

# Q WAP to sort a list using lambda function.
fruits = ["kiwi", "apple", "orange", "mango", "banana"]
sortedList = sorted(fruits, key = lambda x : x)
print(sortedList)

# Q WAP to find square of each element of a list and store them to another empty list.
numList = [1,2,3,4,5,6,7,8,9,10]
sqList = [(lambda x : x**2)(x) for x in numList]
print(sqList)

# Q Using a lambda function to sort a list of strings by the last character
myList = ["apple", "banana", "cherry"]
sortList = sorted(myList, key = lambda x : x[-1])
print(sortList)

# Q WAP to find square of each element of a list and store them to another empty list using lambda function and map function.
lsi = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x : x ** 2, lsi))
print(newList)

# Q Write a Python program to sort a list of tuples using Lambda. Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorList = sorted(tup, key = lambda x : x[1])
print(sorList)

# Q Write a Python program to sort a list of dictionaries using Lambda. Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
listOfDict = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
sortedDict = sorted(listOfDict, key = lambda x : x['make'])
print(sortedDict)

# Q Write a Python program to filter a list of integers using Lambda. Original list of integers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eNum = list(filter(lambda x : (x % 2 == 0), num))
print(eNum)