import math

# Problem 1: Difference between a given number and 17
def difference_from_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

# Problem 2: Test whether a number is within 100 to 1000 or 2000
def within_range(n):
    return (100 <= n <= 1000) or (n == 2000)

# Problem 3: Reverse a string
def reverse_string(s):
    return s[::-1]

# Problem 4: Count upper and lower case letters in a string
def count_upper_lower(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Problem 5: Return a list with distinct elements
def distinct_elements(lst):
    return list(set(lst))

# Problem 6: Print even numbers from a list
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Problem 7: Access a function inside a function
def outer_function(a):
    def inner_function(b):
        return b * 2
    return inner_function(a) + 3

# Problem 8: Function attributes
def student(name, age):
    student.name = name
    student.age = age

# Problem 9: Class `Student` with attributes
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_class(self, student_class):
        self.student_class = student_class

    def display(self):
        print(self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

# Problem 10: Class `Student` with instances
class StudentInstances:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

# Problem 11: Class `Circle` to compute area and perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Problem 12: Class with `get_String` and `print_String`
class StringManipulation:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())


# Function Calls
print(difference_from_17(22))
print(within_range(150))
print(reverse_string("hello"))
upper, lower = count_upper_lower("Hello World")
print(f"Upper case: {upper}, Lower case: {lower}")
print(distinct_elements([1, 2, 2, 3, 4, 4, 5]))
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(outer_function(5))

student("Alice", 21)
print(f"Name: {student.name}, Age: {student.age}")

student_obj = Student(1, "John")
student_obj.set_class("10th Grade")
student_obj.display()

student1 = StudentInstances(1, "John")
student2 = StudentInstances(2, "Alice")
print(f"Student 1 - ID: {student1.student_id}, Name: {student1.student_name}")
print(f"Student 2 - ID: {student2.student_id}, Name: {student2.student_name}")

circle = Circle(5)
print(f"Area: {circle.area()}, Perimeter: {circle.perimeter()}")

str_obj = StringManipulation()
str_obj.get_String()
str_obj.print_String()
