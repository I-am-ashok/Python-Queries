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


def datetimeoperations(value):
    deltpar={"days":0,"hours":0,"minutes":0,"seconds":0}
    keys=deltpar.keys()
    for key in keys:    
        print(f"Format:{key}")
        delta=datetime.timedelta(**{key:value})
        #print(f"Current Date:{datetime.datetime.today().strftime("%x %X %p")}")
        print(f"Delta with {key}={value}: {(datetime.datetime.today()-delta).strftime("%x %X %p")}\n")
    
#datetimeoperations(10)

# Decorators

class decarator:
    def __init__(self):
        self._x=None
    def getx(self):
        return self._x
    def setx(self,value):
        self._x=value
    def delx(self):
        del self._x
    x=property(getx,setx,delx,"This is DocString!!!")

d=decarator()
d.x=10
print(d.getx())


class electricity:
    def __init__(self):
        self._x=None
    @property
    def x(self):
        """This method is a doc string of getter method"""
        return self._x
    @x.setter
    def x(self,value):
        self._x=value
    @x.deleter
    def x(self):
        del self._x
        
e=electricity()
e.x=25
print(e.x)
e.x
print(e.x.__doc__)


