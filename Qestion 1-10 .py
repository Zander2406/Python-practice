#1. Area of a circle 
'''from math import pi
r = float(input("Radius of the circle is = "))
# pi = float(3.14)
Area = pi*r*r 
print("Area of the circle is = ", Area)'''

#2. User first and last name and print them in reverse order with a space between them.
'''firstname = input("User first name = ")
lastname = input("User last name = ") 
print(lastname+" "+firstname)'''

#3. List & Tuple
'''data = input("Enter the data : ")
data = data.split(", ")
# data = 1, 3, 5, 7, 9
print("List = ", list(data))
print("Tuple = ", tuple(data))'''

#4. Display the first and last object from the following list.
'''color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])'''

#5. n+nn+nnn string concatenation
'''n = input("Input the number : ")
print("Total value of n+nn+nnn is = ", (int(n) + int(n+n) + int(n+n+n)))'''

#6. Date difference 
'''from datetime import date as dt
dt1 = dt(2014, 7, 2)
dt2 = dt(2014, 7, 11)
gap = dt2 - dt1 
print(str(gap)[0])'''

#7. Print the calendar of a given month and year.
'''from calendar import month
Sept = month(2022, 9, 3, 2)
print(Sept)'''

#8. Volume of a sphere with radius 6
'''from math import pi
r = 6
print("Volume of the sphere = ", 4/3*pi*r*r*r)'''


#9. Absolute difference
'''number = int(input("Enter the number = "))
print(abs(17 - number))'''

#10.Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
'''a = int(input("Enter the no. = "))
b = int(input("Enter the no. = "))
c = int(input("Enter the no. = "))
sum = a+b+c
if a==b==c: 
    print(3*sum)
else:
    print(sum)
   # or
numbers = input("Enter the numbers: ")
numbers = numbers.split(", ")
numbers = [int(x) for x in numbers]
s = sum(numbers)

if (3 * numbers[0] == s):
    print(3 * s)
else:
    print(s)'''