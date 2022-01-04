# ATM Operations:
#. 1. Display list of options to user: 1. Disposite 2. Withdraw 3. balEnquiry 0. EXIT
#. Methods: validate(), deposite(), withdraw(), balEnquiry

class Atm:
     bal=1000
     def validate(self):
         pin=int(input('enter pin number'))
         if pin!=0:
            print('press 1,2,3,0 for below options')
            print('1.Deposite')
            print('2.Withdraw')
            print('3.balEnquiry')
            print('0.exit')
            n=(int(input()))
            if n==1:
               a=int(input("enter the deposite amount"))
               self.bal=self.bal+a
               print("Current Balance",self.bal)
            elif n==2:
                b=int(input("enter the withdraw amount"))
                self.bal=self.bal-b
                print("Current Balance",self.bal)
            elif n==3:
                print("Current Balance",self.bal)   
            elif n==0:
                print('exit')
         else:
             print('invalid pin')
obj=Atm()
obj.validate()     
     

   
    

