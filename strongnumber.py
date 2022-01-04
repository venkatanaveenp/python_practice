a=1
b=100000

p=0
for i in range(a,b+1):
    
    temp=i
   
    d=str(i)
    c=len(d)
    for j in range(c):
       
        r=i%10
        i=i//10
      
        j=1
        for k in range(1,r+1):
            j=j*k
       
        p=p+j
   
    if temp==p:
        p=0
        print(temp,":strong")
    else:
        p=0
    
        
            
            
            
        
