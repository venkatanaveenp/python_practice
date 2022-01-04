#check palindrome
rev=0 
n=int(input("enter n value")) 
temp=n; 
while(n!=0): 
    rem=n%10 
    rev=rev*10+rem
    n=n//10
if temp==rev: 
    print("palindrome") 
else:
    print("not a palindrome")