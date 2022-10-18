#21.Write a Python program to solve (x + y) * (x + y).
'''x = int(input("Enter X = "))
y = int(input("Enter Y = "))
# print((x+y)*(x+y))
# print("Value of (x+y)*(x+y) is =  ", (x+y)*(x+y))

print(f"({x} + {y})^2 = {(x+y)**2}")'''

#22.Calculate Amount with the help of Simple Interest formula.
'''p = float(input("Enter the Principle = "))
r = float(input("Enter the Rate = "))
t = float(input("Enter the Time = "))
# S.I. = ((p*t*r)/100 + p)
CI =float(p*(1+r/100)**t)
print(f"The total Amount is = {round(CI, 2)}")'''

#23.Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
'''Cordinate1 = input("Enter the Cordinate 1 i.e. X1, Y1 = ")
Cordinate2 = input("Enter the Cordinate 2 i.e. X2, Y2 = ")
Cordinate1 = Cordinate1.split(", ")
Cordinate1 = [int(x) for x in Cordinate1]
Cordinate2 = Cordinate2.split(", ")
Cordinate2 = [int(x) for x in Cordinate2]
Distance = ((Cordinate2[0]-Cordinate1[0])**2 + (Cordinate2[1]-Cordinate1[1])**2)**0.5
print(f"The distance between Cordinate1 and Cordinate2 is = {round(Distance, 3)}")'''

#24.Write a Python program to print without newline or space.
'''lst=[25, 456, 78, 68, 12, 111258]
for i in lst :
    print(i, end=" ")'''

#25.Write a Python program to get the current filename.
import os 
f = os.path.basename(__file__)
print(f)











