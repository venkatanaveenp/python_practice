#1. Accept two integer values from the user and return their product. If the product is greater than 1000, then return their sum
a=int(input("enter the value1="))
b=int(input("enter the value2="))
c=a*b
print("product of two number",c)


if c>1000:
    print("product is greater than 1000")
    sum=a+b
    print("sum of two numbers=",sum)
