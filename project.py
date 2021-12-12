class Cars:
    def __init__(self):
        self.com_name=" "
        self.name=" "
        self.seatingspace=0
        self.mileage=0
        self.rating=0
        self.topspeed=0
        self.pr=" "

    def display(self):
        print(ci.com_name,ci.name,ci.ss,ci.mileage,ci.rt,ci.sp,ci.pr)
choice=0
while(choice!=5):
    print("\t\t\t *****W E L C O M E    TO   CAR   GARAGE***** \t\t\t\t\n")
    print("\t\t\t\t1. E N T E R  D E T A I L S \t\t\t\t\n")
    print("\t\t\t\t2. D I S P L A Y   D E T A I L S \t\t\t\t")
    print("\t\t\t\t3. P R I C E \t\t\t\t\n")
    print("\t\t\t\t4. E X I T \t\t\t\t")
    choice=int(input("Enter your choice:"))

    if (choice==1):
        n=int(input("Enter the no. of cars:"))
        l=()
        for i in range(n):
            ci=Cars()
            ci.com_name=input("Enter company name:")
            ci.name=input("Enter name:")
            ci.ss=int(input("Enter seating capacity:"))
            ci.mileage=float(input("Enter Mileage:"))
            ci.rt=float(input("Enter ratings:"))
            ci.sp=int(input("Enter top speed:"))
            ci.pr=int(input("Enter price:"))
            l=l+(ci.com_name,ci.name,ci.ss,ci.mileage,ci.rt,ci.sp,ci.pr)
            
            string=str(l)
            f=open("PROJECT.TXT","a")
            f.write(string)
            f.close()
            l=()
    if (choice==2):
          f=open("PROJECT.TXT","r")
          print(f.read())
          f.close()
    if (choice==3):
        price=int(input("Enter price range:"))
        for i in l:
            if i[6]<price:
                print(i)
    if (choice==4):
        exit(0)
            
          
        
    

        
        
