# Inheritance
# # The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
# # The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating it from scratch.
# # In inheritance, the child class acquires all the data members, properties, and functions from the parent class. Also, a child class can also provide its specific implementation to the methods of the parent class.
# # Types Of Inheritance :- Single, Multiple, Multilevel, Hierarchical and Hybrid.

# Single Inheritance
# Parent Class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')
# Create object of Car
car = Car()
# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()

# Multiple Inheritance
# Parent Class 1
class Person:
    def person_info(self, name, age) :
        print("Inside Person Class")
        print("Name :-", name, "Age :-", age)

# Parent Class 2
class Company:
    def company_info(self, comName, location):
        print("Inside Company Class")
        print("Company Name :-", comName, "Location :-", location)
# Child Class
class Employee(Person, Company):
    def Emp_Info(self, salary, skill):
        print("Inside Employee Child Class")
        print("Salary :-", salary, "Skills :-", skill)
emp = Employee()
emp.person_info("Yash", 23)
emp.company_info("KVONTech", "Jaipur")
emp.Emp_Info(1200000, "WebD")


# Multilevel Inheritance :- A chain of classes is called multilevel inheritance.
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')
# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')
# access Vehicle's and Car info using SportsCar object
SportsCar().Vehicle_info()
SportsCar().car_info()
SportsCar().sports_car_info()


# Hierarchical Inheritance :- One parent class and multiple child classes.
class Vehicle:
    def info(self):
        print("This is Vechicle")
class Car(Vehicle):
    def carInfo(self, name):
        print("Car Name id :-", name)
class Truck(Vehicle):
    def truckInfo(self, name):
        print("Truck Name is :-", name)
obj1 = Car()
obj1.info()
obj1.carInfo('BMW')
obj2 = Truck()
obj2.info()
obj2.truckInfo("Volvo")


# Hybrid Inheritance :- When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.
class Vehicle:
    def vehicleInfo(self):
        print("Inside Vehicle Class")
class Car(Vehicle):
    def carInfo(self):
        print("Inside Car Class")
class Truck(Vehicle):
    def truckInfo(self):
        print("Inside Truck Class")

class SportsCar(Car, Vehicle):
    def spoCarInfo(self):
        print("Inside Sports Car Class")
SportsCar().vehicleInfo()
SportsCar().carInfo()
# SportsCar().truckInfo()
SportsCar().spoCarInfo()


class A:
    def process(self):
        print(" In class A")

class B(A):
    def process(self):
        print(" In class B")

class C(B, A):
    def process(self):
        print(" In class C")

# Creating object of C class
# C1 = C()
# C1.process()
print(C.mro())




# Iterator
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# StopIteration :- To prevent the iteration from going on forever, we can use the StopIteration statement.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



# Polymorphism
class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)
        
    def work(self):
        print(self.name, 'working as a', self.profession)
        
        
class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print('Details:', self.name, self.color, self.price)
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')
# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')
    def change_gear(self):
        print('Car change 7 gear')
# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()