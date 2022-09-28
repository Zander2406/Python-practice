#11. Given number is even or odd
'''a = int(input("Enter a number : ")) %2
# type = a % 2
if a > 0:
    print("This is an odd number")
else:
    print("This is an even number")'''

#12. Area of a Triangle
'''b = int(input("Base of the triangle : "))
h = int(input("Height of the triangle : "))
area = 1/2*b*h
print("Area of the triangle is : ", area)'''

#13. Sum of two given integers. However, if the sum is between 15 to 20 it will return 20
'''a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
sum = a+b
if sum > 15 and sum < 20:
# if sum in range(15, 20):
    print(20)
else:
    print(sum)'''

#14.
'''word = input("Enter any word : ")
if str("ls") in word:
    print(word)
else:
    print(str("ls")+word)'''

#15. Count the number 4 in a given list
'''lst = input("Enter the numbers : ")
lst = lst.split(", ")
lst = [int(x) for x in lst]
lst_count = lst.count(4)
print(lst_count)'''

#16. Test whether a passed letter is a vowel or not.
'''letter = input("Enter a letter : ")
lst = ("a" , "e", "i", "o", "u")
if letter in lst:
    print("This letter is vowel.")
else:
    print("It is consonant.")'''

#17. Concatenate all elements in a list into a string and return it.
'''lst = input("Enter any element : ")
lst = lst.split(" ")
rslt =  ""
for element in lst:
    rslt = rslt + element 
print(rslt)'''

#18.Print even number from a given list.
'''numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]'''
'''final_list = []
for number in numbers:
    if number < 237:
        if number % 2 == 0:
            final_list.append(number)
print(final_list)'''

# or

'''final_list = []
numbers.sort()
for number in numbers:
    if number > 237:
        break
    if number % 2 == 0:
        final_list.append(number)
print(final_list)'''




















