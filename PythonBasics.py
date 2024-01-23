
#calculate Area of a trangle
def Area():
    B=float(input("Enter a number for Base: "))
    H=float(input("Enter a number for Height: "))
    return 0.5*B*H
# Swap Two variables
def swap():
    B=float(input("Enter a number for Base: "))
    H=float(input("Enter a number for Height: "))
    H,B=B,H
    print(f"B vale is {B}, H value is {H}")

# Palindrome check

def polindrome():
    Num=input("Please enter a Number ")
    check=Num[::-1]
    print(check)
    if Num==check:
        print(f"{Num} is polindrome")
    else:
        print(f"{Num} is not polindrome")

# print a pramid
def Pyramid():
    row=int(input("Eneter row num to print the pyramid "))
    for r in range(row):
        print(" "*(row-r-1)+'*'*(2*r+1))
    print("Printing Trangle in reverse order ")
    for r in range(row,0,-1):
        for j in range(row-r):
            print(" ",end=" ")
        for k in range(2 * r - 1):
            print("*",end=' ')
        print("\r")

# check if te number is prime or not

def primeorNot():
    IsPrime=False
    Num=int(input("Enter a number to check for the prime or not? "))
    if Num==1:
        print(f"{Num} is not a Prime")
    else:
        if Num>1:
            for i in range(2,Num):
                if (Num%i)==0:
                    IsPrime=True
                    break
    if IsPrime:
        print(f"{Num} is not a Prime")
    else:
        print(f"{Num} is Prime")


# Print Fibancci series for the given number

def febancci():
    Num=int(input("Enter a number to print the series "))
    count=0
    n1,n2=0,1
    if Num<0:
        print("Enter a positive number")
    elif Num==1:
        print(f"{Num} febanacci series upto {Num} is: {n1}")
    else:
        print("Fibanacci series is :")
        while count<Num:
            print(n1)
            result=n1+n2
            n1,n2=n2,result
            count+=1

# check a number is armstrong or not?

def Armstrong():
    Num=int(input("Enter a number to check for Armstrong or not "))
    Tempnum=Num
    length=len(str(Num))
    print(f"length of {Num} is {length}")
    sumofpower=0
    while Tempnum>0:
        digit=Tempnum%10
        sumofpower+=digit**length
        Tempnum//=10
    if Num==sumofpower:
        print(f"{Num} is ArmStrong Number")
    else:
        print(f"{Num} is not an armstrong")




def dicti():
    dict={}
    str=input("Eneterastring")
    l=list(str)
    for chr in l:
        print(chr)
        if chr in dict:
            dict[chr]+=1
        else:
            dict[chr]=1
    return dict

def printtime():
    import datetime
    time=str(datetime.datetime.now())[11:19]
    time=str(datetime.datetime.now())[11:len(str(datetime.datetime.now()))]
    print(time)
    print(datetime.datetime.now().strftime("%H:%M:%S"))


def dictsort():
    sdict={'banana': 1,'apple': 3, 'date': 4, 'cherry': 2 }
    sorteddf=dict(sorted(sdict.items()))
    print(sorteddf)
""" 
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
"""

def matrix():
    row,col=map(int,input("Enter Row and columns for matrix:").split(","))
    matrx=[[0 for j in range(col)] for i in range(row)]
    print(matrx)
    for i in range(row):
        for j in range(col):
            matrx[i][j]=i*j
    for row in matrx:
        print(row)

def wordsort():
    string=input("Enter the sentence: ")
    l=[l.lower() for l in string.split(" ")]
    words=sorted(l)
    words=','.join(words)
    print(words)

def removedup():
    string=input("Enetr a sentence to get the distinct words in an order: ")
    words=[ word.lower() for word in string.split(" ")]
    words=sorted(list(set(sorted(words))))
    words=",".join(words)
    print(words)

#removedup()
#Write a program that accepts a sentence and calculate the number of letters and digits.

def let_and_dig():
    sent=input("Enter the sentence to find the digit and letters: ")
    dict={"Digit":0,"Letters":0}
    for chr in sent:
        if chr.isdigit():
            dict["Digit"] +=1
        elif chr.isalpha():
            dict["Letters"] +=1
    for key,value in dict.items():
        print(f"{key}={value}")

# check the entered password is as per recommendations or not? 
# at least 1 lower case letter
# at least 1 upper case letter
# at least 1 special case letter
# at least 1 digit
# password length between 8 to 12

def passwordcheck():
    import re
    passwordlist=input("Eneter the passwords list to check: ")
    passwords=passwordlist.split(",")
    validpass_words=[]
    for password in passwords:
        print(password)
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&])(?=.*\d).{8,12}$",password):
            validpass_words.append(password)
        else:
            pass
    print(validpass_words)


# Define a class with a generator which can iterate the numbers, which are divisible by 11, 
# between a given range 0 and n

class divide:
    def __init__(self,n):
        self.n=n
        
    def gen_divide(self,d):
        for num in range(self.n+1):
            if num%d==0:
                yield num

#n,d=map(int,input("Eneter the Range to genarate the divisibles by number").split(","))
#nums=divide(n).gen_divide(d)

#for num in nums:
#    print(num)

# Genarators func

def febanaccigen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
 
febna=febanaccigen()       
#for _ in range(5):
    #print(next(febna))
    
#Please write a program to compress and decompress the CustomerNames

def encrypt():
    import zlib
    compressed_Names=[]
    decompressed_Names=[]
    Names=["Asok","Pavan","Anil","Sruthi","Sahasra"]
    for name in Names:
        compressed_Names.append(zlib.compress(str(name).encode()))
    for name in compressed_Names:
        decompressed_Names.append(zlib.decompress(name).decode())
    
    print("Names Are: ")
    print(Names)
    print("Encrepted Names Are: ")
    print(compressed_Names)
    print("Decrepted Names Are: ")
    print(decompressed_Names)
import math

class arthemetics:
    def __init__(self):
        self.p=0
        self.r=0
        self.t=0
        
        self.Num_Area=input("Which Operation you want to perform (Numerical\\Area\\Money) ? ")
        if self.Num_Area=='Numerical':
            self.operation=input("Which Operation you want to perform (sum\\subtract\\Mul\Div) ? ")
        elif self.Num_Area=='Area':
            self.operation=input("Which Shape Area you want to Calculate (Triangle\\Square\\Rectangle\\Perallelogram\\Circle\\Ellipse\\Sector\\Trapezium) ? ")
        elif self.Num_Area=='Money':
            self.operation=input("Which Intrest you want to Calculate (SimpleIntrest OR CompoundIntrest) ? ")
        else:
            pass
            
            
   
    def AR_OP(self):
        if self.Num_Area=='Numerical':
            if self.operation=='sum':
                self.a=input("Enter comma separated values to sum: ").split(",")
                arr=self.a
                result=0
                for val in arr:
                    result+=int(val)
                return result
                
            elif self.operation=='subtract':
                self.a,self.b=map(int,input("Enter 2 comma sepated values to subtract: ").split(","))
                return self.a-self.b
            elif self.operation=='Mul':
                self.a,self.b=map(int,input("Enter 2 comma sepated values to Multiply: ").split(","))
                return self.a*self.b
            elif self.operation=='Div':
                self.a,self.b=map(int,input("Enter 2 comma sepated values to Divide: ").split(","))
                if self.b==0:
                    print("Number is not divisible by 0")
                else:
                    return self.a/self.b
        #Triangle\Square\Rectangle\Perallelogram\Circle\Ellipse\Sector\Trapezium
        elif self.Num_Area=='Area':
            if self.operation=='Triangle':
                self.b,self.h=map(int,input("Enter comma separated Base and height values ").split(","))
                return round(0.5*self.b*self.h,2)
            elif self.operation=='Square':
                self.a=int(input("Enter length of a side of a suare: "))
                return round(self.a*self.a,2)
            elif self.operation=='Rectangle':
                self.w,self.h=map(int,input("Enter comma separated Width and height of a Rectangle: ").split(","))
                return round(self.w*self.h,2)
            elif self.operation=='Perallelogram':
                self.b,self.h=map(int,input("Enter comma separated Base and height values ").split(","))
                return round(self.b*self.h,2)
            elif self.operation=='Trapezium':
                self.a, self.b,self.h=map(int,input("Enter comma separated two lengths of sides and height of Trapezium ").split(","))
                return round(0.5*(self.a+self.b)*self.h,2)
            elif self.operation=='Circle':
                self.r=int(input("Enter radious of a circle: "))
                return round(math.pi*self.r**2,2)
            elif self.operation=='Ellipse':
                self.a,self.b=map(int,input("Enter comma separated semi-major axis and semi-minor axis lengths: ").split(","))
                return round(math.pi*self.a*self.b,2)
            elif self.operation=='Sector':
                self.r,self.theta=map(int,input("Enter comma separated radious and Theta values for a Sector: ").split(","))
                return round(0.5*self.r**2*(self.theta*(math.pi/180)),2)
        elif self.Num_Area=='Money':
            if self.operation=='SimpleIntrest':
                self.p,self.r,self.t=map(int,input("Enter comma separated Principle,RateofIntrest per year,Time in months: ").split(","))
                return self.p,self.r,self.t,round(self.p*(self.r/(12*100))*self.t,2)
            elif self.operation=='CompoundIntrest':
                self.p,self.r,self.t=map(int,input("Enter comma separated Principle,RateofIntrest per year,Time in months: ").split(","))
                return self.p,self.r,self.t,round((self.p*(1+(self.r/(12*100)))**(12*(self.t/12)))-self.p,2)
                
                
                
            

def PerformArthematicOperations():
    cls=arthemetics()
    if cls.Num_Area=='Area' and cls.operation in["Triangle","Square","Rectangle","Perallelogram","Circle","Ellipse","Sector","Trapezium"]:
        print(f"Area of {cls.operation} is {cls.AR_OP()}")
    elif cls.Num_Area=='Money' and cls.operation in ["SimpleIntrest","CompoundIntrest"]:
        p,r,t,interst=cls.AR_OP()
        print(f"{cls.operation} of principle {p},% of intrest rate per year is {r} and timePeriod {t} Months is {interst}")
    elif cls.Num_Area=='Numerical' and cls.operation in ['sum','subtract','Mul','Div']:
        print(f"{cls.operation} is {cls.AR_OP()}")        
    useroption=input("Do you want continue with other operation Y\\N ? ")
    if useroption=='Y':
        return PerformArthematicOperations()
    else:
        print("Thank you closing the application!!")
        exit 
       
    

PerformArthematicOperations()
#encrypt()
#passwordcheck()
#let_and_dig()
#wordsort()
#matrix()
#dictsort()
#printtime()
#print(dicti())
#Armstrong()
#febancci()
#primeorNot()
#Pyramid()        
#polindrome()
#print(f"Area of Trangle is {Area(B,H)}")
#swap(B,H)


import math

class Arithmetic:
    def _init_(self):
        self.p = 0
        self.r = 0
        self.t = 0
        self.Num_Area = input("Which operation you want to perform (Numerical\\Area\\Money) ? ")

        if self.Num_Area == 'Numerical':
            self.operation = input("Which operation you want to perform (sum\\subtract\\Mul\\Div) ? ")
        elif self.Num_Area == 'Area':
            self.operation = input("Which shape area you want to calculate (Triangle\\Square\\Rectangle\\Parallelogram\\Circle\\Ellipse\\Sector\\Trapezium) ? ")
        elif self.Num_Area == 'Money':
            self.operation = input("Which interest you want to calculate (SimpleInterest OR CompoundInterest) ? ")

    def perform_arithmetic_operation(self):
        if self.Num_Area == 'Numerical':
            if self.operation == 'sum':
                values = map(int, input("Enter comma-separated values to sum: ").split(","))
                return sum(values)
            elif self.operation == 'subtract':
                a, b = map(int, input("Enter 2 comma-separated values to subtract: ").split(","))
                return a - b
            elif self.operation == 'Mul':
                a, b = map(int, input("Enter 2 comma-separated values to multiply: ").split(","))
                return a * b
            elif self.operation == 'Div':
                a, b = map(int, input("Enter 2 comma-separated values to divide: ").split(","))
                return a / b if b != 0 else "Number is not divisible by 0"
        
        elif self.Num_Area == 'Area':
            if self.operation in ["Triangle", "Square", "Rectangle", "Parallelogram", "Circle", "Ellipse", "Sector", "Trapezium"]:
                dimensions = map(int, input(f"Enter comma-separated dimensions for {self.operation}: ").split(","))
                return self.calculate_area(self.operation, *dimensions)

        elif self.Num_Area == 'Money':
            if self.operation in ["SimpleInterest", "CompoundInterest"]:
                p, r, t = map(int, input("Enter comma-separated Principle, Rate of Interest per year, Time in months: ").split(","))
                return self.calculate_interest(self.operation, p, r, t)

    def calculate_area(self, shape, *args):
        if shape == 'Triangle':
            b, h = args
            return round(0.5 * b * h, 2)
        elif shape == 'Square':
            a, = args
            return round(a * a, 2)
        elif shape == 'Rectangle':
            w, h = args
            return round(w * h, 2)
        elif shape == 'Parallelogram':
            b, h = args
            return round(b * h, 2)
        elif shape == 'Trapezium':
            a, b, h = args
            return round(0.5 * (a + b) * h, 2)
        elif shape == 'Circle':
            r, = args
            return round(math.pi * r**2, 2)
        elif shape == 'Ellipse':
            a, b = args
            return round(math.pi * a * b, 2)
        elif shape == 'Sector':
            r, theta = args
            return round(0.5 * r**2 * (theta * (math.pi/180)), 2)

    def calculate_interest(self, interest_type, p, r, t):
        if interest_type == 'SimpleInterest':
            return p, r, t, round((p * (r / (12 * 100)) * t), 2)
        elif interest_type == 'CompoundInterest':
            return p, r, t, round((p * (1 + (r / (12 * 100)))**(12 * (t / 12))) - p, 2)

def perform_arithmetic_operations():
    arithmetic_obj = Arithmetic()
    result = arithmetic_obj.perform_arithmetic_operation()

    if isinstance(result, tuple):
        p, r, t, interest = result
        print(f"{arithmetic_obj.operation} of principle {p}, % of interest rate per year is {r} and time period {t} months is {interest}")
    elif isinstance(result, str):
        print(result)
    else:
        print(f"{arithmetic_obj.operation} is {result}")

    user_option = input("Do you want to continue with another operation Y\\N ? ")
    if user_option == 'Y':
        perform_arithmetic_operations()
    else:
        print("Thank you, closing the application!!")

#perform_arithmetic_operations()