
import math
# 1
print("Twinkle, twinkle, little star, \nHow I wonder what you are! \n Up above the world so high, \n Like a diamond in the sky. \nTwinkle, twinkle, little star, \nHow I wonder what you are!")

#2
first = input("enter first name\n")
second = input("enter second name \n")
print(second +" "+ first)

#3
r = input("enter the radius of circle")
area = int (r) *3.14* int(r)
print(area)

#4
color_list=["red", "green ", "white", "black"]
print(color_list[0])
print(color_list[3])

#5
n = input("enter digit n")
x = int(n) + int(n)*int(n)+int(n)*int(n)*int(n)
print(x)

#6
num = input("Enter a sequence of comma-separated numbers: ")
num_list = numbers.split(",")
num_tuple = tuple(num_list)
print("List:", num_list)
print("Tuple:", num_tuple)

#7 
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:",fahrenheit )

#8
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
  # swaping
a, b = b, a
   # Increment one of them
a += 1
print("After swapping and incrementing, a =", a, "and b =", b)

#9 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#10
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is a leap year.")
else:
    print(year,"is not a leap year.")

#11
x1 = float(input("enter x1\n"))
x2 = float(input("enter x2\n"))
y1 = float(input("enter y1\n"))
y2 = float(input("enter y2\n"))
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(" ", euclidean_distance)

#12 
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")

#13
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

compound_interest = principal * (1 + rate / 100) ** time - principal
print(f"The compound interest is: {compound_interest}")

#14
n = int(input("Enter a positive integer: "))
if n >1 :
    for i in range(2, n):
        if n % i == 0:
            print(n ," is not a prime number.")
            break
        else:
            print(n, " is a prime number.")
else :
    print(n , "not prime")

15

t = int(input("enter the number t"))
addition =0
for i in range(1, t+1):
    addition = addition + (i**2)
    
print(addition)
