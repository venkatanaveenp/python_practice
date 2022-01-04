# Python Program to find the area of triangle

# inputs from the user
a = float(input('Enter length of first side: '))
b = float(input('Enter length of second side: '))
c = float(input('Enter length of third side: '))

# Calculating the semi-perimeter
s = (a + b + c) / 2

# Calculating the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is ' ,area)