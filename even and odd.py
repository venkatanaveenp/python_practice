n=int(input("enter n value="))
i=1 
print("even number")
while(i<=n):
    if(i%2==0): 
        print(i)
    i=i+1
    
print("odd numbers")
for i in range(1,10):
    if(i%2!=0):
        print(i)
    i=i+1