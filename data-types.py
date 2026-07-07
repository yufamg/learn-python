import json
import math


intro = "Hello, World!"
print(intro)


# Integer
age = 20
print(age)

# Float
pi = 3.14159
print(pi)

# String
name = "John"
print(name)

# Boolean
is_student = True
print(is_student)

# List
numbers = [1, 2, 3, 4, 5]
names = [x for x in range(20) if x % 2 == 0]
def mapnums(nums):
    print(nums)
    return nums * 2
names = map(mapnums, names)
print(f'{list(names)}')
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers))
# print(sorted(numbers))
# print(list(reversed(numbers)))
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])

# Dictionary
person = {"name": "John", "age": 20, "is_student": True}
print(person)
print(type(person))
person["name"] = "Jane"
# Tuple
coordinates = (1, 2, 3)
print(coordinates)
tuple1 = ("两点水", "twowter", "liangdianshui", [123, 456])
print(tuple1)
print(type(tuple1))
del tuple1


# Set
colors = {"red", "green", "blue"}
colors.add("yellow")
print(sorted(colors))

print(ord("A"), ord("B"), ord("C"))

print(int("123"))
print(int(123.22))
