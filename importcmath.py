import cmath
  
a=int(input("enter the a value="))
b=int(input("enter the b value="))
c=int(input("enter the c value="))
  
# calculating  the discriminant
dis = (b**2) - (4 * a*c)
  
# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
  
# printing the results
print('The roots are')
print(ans1)
print(ans2)