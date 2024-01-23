# Working with Datetime Functions
import datetime
def dateformats():
    for format in ["%I:%M:%S %p","%A %B 20%y %X %p","%A","%a","%b","%B","%c","%f","%j","%m","%p","%w","%x","%z","%X","%y","%H","%M","%S","%W","%U","%Z"]:
        d= datetime.datetime.now().strftime(str(format))
        print(f"With format {format} The Date Reprasented as {d} ")



def tables():
    n=int(input("Enter the table you want? "))
    for i in range(1,11):
        print(f"{n} x {i}={n*i}")
    useroption=input("Do you want to continue? Y\\N: ")
    if useroption=='Y':
        return tables()
    else:
        print("Thank you have a grate day!")
import calendar
def cal():
    for month in [1]:# [1,2,3,4,5,6,7,8,9,10,11,12]:
        calen=calendar.month(2024,month)
        print(calen,end=' ')
        print("*"*100)
        for month in calendar.month_name[1:]:
            month=month.upper()
            monthnum=getattr(calendar,month)
            if monthnum==1:
                print(f"The Month Number of {month} is {monthnum}")
            else:
                print(f"{month} is {monthnum}")
            

#cal()

from random import shuffle

def Random():
    for c in range(100):
       yield ascii(c) 
    
#shu=list(Random())
#print(shu)

import re
def remodule():
    re_split=re.split(" ","ashokkumar 124ashok123 457_ashok")
    re_sub=re.sub("k","#","ashokkumar 124ashok123457 ashok")
    re_subn=re.subn("k","#","ashokkumar 124ashok123457 ashok")
    print(re_split)
    print(re_sub)
    print(re_subn)

list=[]
def listoper():
    list.append("Ashok")
    list.insert(1,34)
    list.extend("B.Tech")    
    print(list)
    
#listoper()

# write a program to check the number is prime/odd/even ?

def checknum():
    n=int(input("Enter the number to check  either prime/Odd/Even? ==>"))
    if n==1:
        return "it is Odd and not prime"
    elif n%2==0:
        return "Num is prime and it is Even" if n==2 else "Num is even and not prime"
    elif n%2!=0:
        for l in range(2,n):
            if n%l==0:
                return "Num is not Prime but it is odd"
            
    return "Num is prime and it is also odd"

def recursive():
    print(checknum())
    useroption=input("Do you want to continue? Y\\N ")
    if useroption=='Y':
        while useroption=='Y':
            print(checknum())
            useroption=input("Do you want to continue? Y\\N ")
    else:
        pass
    return "closing the application!!"

#print(recursive())

def printprimenum():
    primes=[]
    n=int(input("Prime numbers you want to print till: "))
    def isprime(n):
        if n<2:
            return True
        for p in range(2,int(n**0.5)+1):
            if n%p==0:
                return False
        return True
        
    for p in range(2,n+1):
        if isprime(p):
            print(p,end=" ")

#printprimenum()

def febanacci(n):
    a,b=0,1
    for _ in range(n):
     yield a
     a,b=b,a+b   
result=[]
result.extend(febanacci(10))
print(result)






