#6. Python program to multiply all numbers of a list.
a = [11, 22, 33, 44, 55]
print(a)
b=int(input("enter the multiply="))
f=[]

for i in a:
    c=b*i
    f.append(c)
print("multiply of",b,"is",f)
    
