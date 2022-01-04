class Atm:
    bal=10000
    total=0
    def validate(self):
        password=int(input("enter the password"))
        if password==1432:
            print("password validate")
            print('''press 0,1,2,3 for below options.
            0.exit
            1.deposite
            2.with draw
            3.balancewnquiry
            ''')
            a=int(input())
            if a==1:
                b=int(input("enter the deposite amount"))
                self.bal=self.bal+b
                print("Current Balance",self.bal)
            elif a==2:
                c=int(input("enter the withdraw amount"))
                self.bal=self.bal-c
                print("Current Balance",self.bal)
            elif a==3:
                print("Current Balance",self.bal)
            else:
                print("exit")
        else:
            print("password is invalid")
                
obj=Atm()
obj.validate()