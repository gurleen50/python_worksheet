#1
#1 st with direct functions

L = [11, 12, 13, 14]

# (i) Add 50 and 60 to L
L.append(50)
L.append(60)
print("After adding 50 and 60:", L)

# (ii) Remove 11 and 13 from L
L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)

# (iii) Sort L in ascending order
L.sort()
print("Sorted in ascending order:", L)

# (iv) Sort L in descending order
L.sort(reverse=True)
print("Sorted in descending order:", L)

# (v) Search for 13 in L
found = 13 in L
print("Is 13 in L?:", found)

# (vi) Count the number of elements in L
count = len(L)
print("Number of elements in L:", count)

# (vii) Sum all the elements in L
total_sum = sum(L)
print("Sum of all elements in L:", total_sum)

# (viii) Sum all ODD numbers in L
odd_sum = sum(num for num in L if num % 2 != 0)
print("Sum of all odd numbers in L:", odd_sum)

# (ix) Sum all EVEN numbers in L
even_sum = sum(num for num in L if num % 2 == 0)
print("Sum of all even numbers in L:", even_sum)

# (x) Sum all PRIME numbers in L
def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True

prime_sum = sum(num for num in L if is_prime(num))
print("Sum of all prime numbers in L:", prime_sum)

# (xi) Clear all elements in L
L.clear()
print("After clearing L:", L)

# (xii) Delete L
del L


#1 st without direct functions

L = [11, 12, 13, 14]

# (i) Manually add 50 and 60 to L
L = L + [50, 60]
print("After adding 50 and 60:", L)

# (ii) Manually remove 11 and 13 from L
L = [x for x in L if x not in [11, 13]]
print("After removing 11 and 13:", L)

# (iii) Manually sort L in ascending order (using bubble sort)
for i in range(len(L)):
    for j in range(0, len(L)-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("Sorted in ascending order:", L)

# (iv) Manually sort L in descending order (using bubble sort and reversing)
for i in range(len(L)):
    for j in range(0, len(L)-i-1):
        if L[j] < L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("Sorted in descending order:", L)

# (v) Manually search for 13 in L (linear search)
found = False
for num in L:
    if num == 13:
        found = True
        break
print("Is 13 in L?:", found)

# (vi) Manually count the number of elements in L
count = 0
for _ in L:
    count += 1
print("Number of elements in L:", count)

# (vii) Manually sum all the elements in L
total_sum = 0
for num in L:
    total_sum += num
print("Sum of all elements in L:", total_sum)

# (viii) Manually sum all odd numbers in L
odd_sum = 0
for num in L:
    if num % 2 != 0:
        odd_sum += num
print("Sum of all odd numbers in L:", odd_sum)

# (ix) Manually sum all even numbers in L
even_sum = 0
for num in L:
    if num % 2 == 0:
        even_sum += num
print("Sum of all even numbers in L:", even_sum)

# (x) Manually sum all prime numbers in L
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_sum = 0
for num in L:
    if is_prime(num):
        prime_sum += num
print("Sum of all prime numbers in L:", prime_sum)

# (xi) Manually clear all elements in L
L = []
print("After clearing L:", L)

# (xii) Delete L
del L



#  2

numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
print("Sum of all items:", total_sum)

# 3
numbers = [1, 2, 3, 4, 5]
total_product = 1
for num in numbers:
    total_product *= num
print("Product of all items:", total_product)


#4
array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(array)


# 5
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) Add new entry with key=8 and value=8.8
D[8] = 8.8
print("After adding key=8:", D)

# (ii) Remove key=2
del D[2]
print("After removing key=2:", D)

# (iii) Check if key=6 is present
key_present = 6 in D
print("Is key=6 present?:", key_present)

# (iv) Count the number of elements in D
element_count = len(D)
print("Number of elements in D:", element_count)

# (v) Add all values in D
total_value_sum = sum(D.values())
print("Sum of all values in D:", total_value_sum)

# (vi) Update the value of key=3 to 7.1
D[3] = 7.1
print("After updating key=3:", D)

# (vii) Clear the dictionary
D.clear()
print("After clearing D:", D)


#6

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) Add 55 and 66 to S1
S1.add(55)
S1.add(66)
print("After adding 55 and 66:", S1)

# (ii) Remove 10 and 30 from S1
S1.discard(10)
S1.discard(30)
print("After removing 10 and 30:", S1)

# (iii) Check if 40 is present in S1
is_present = 40 in S1
print("Is 40 present in S1?:", is_present)

# (iv) Union of S1 and S2
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)

# (v) Intersection of S1 and S2
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)

# (vi) S1 - S2 (difference)
difference_set = S1.difference(S2)
print("S1 - S2:", difference_set)

# 7
import random
import string

# (i) Print 100 random strings of length between 6 and 8
for _ in range(100):
    length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    print(random_string)

# (ii) Print all prime numbers between 600 and 800

for num in range(600, 801):
    b = True
    
    for i in range(2, num+1):
        if num % i == 0:
    
            print(num, "not prime")
            break
        else:
            print(num, "is prime")






# (iii) Print all numbers between 100 and 1000 that are divisible by 7 and 9
divisible_by_7_and_9 = [num for num in range(100, 1001) if num % 7 == 0 and num % 9 == 0]
print("Numbers divisible by 7 and 9 between 100 and 1000:", divisible_by_7_and_9)


# 8
exam_date = (11, 12, 2014)
print("The examination will start from: ", exam_date[0],exam_date[1],exam_date[2] )


# 9

numbers = [10, 15, 23, 40, 55, 60, 72]
for num in numbers:
    if num % 5 == 0:
        print(num)


#10
num = int(input("Enter a number: "))
if num %2==0:
    print("num even")

else:
    print("print false")


#11
text = "Emma is a good developer. Emma also loves to code."
count = text.count("Emma")
print(f"The substring 'Emma' appears {count} times.")

#12

# Given two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]

# Initialize the new list
new_list = []

# Add odd numbers from list1 to new_list
for num in list1:
    if num % 2 != 0:  # Check if the number is odd
        new_list.append(num)

# Add even numbers from list2 to new_list
for num in list2:
    if num % 2 == 0:  # Check if the number is even
        new_list.append(num)

# Print the result
print("New list:", new_list)

