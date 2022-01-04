a=[]
length=int(input("enter the length of list a[]"))
j=False
print("enter values")
for i in range(1,length+1):
    v=int(input())
    a.append(v)
print("list of elements",a)
c=int(input("enter search value"))

for even in a:
    if even==c:
        j=True
        break
if j:
    print("element found")
else:
    print("element not found")