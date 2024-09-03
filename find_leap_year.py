year = int(input("Enter a year: "))

def isLeapYear(year):
    if(year%400==0 and year%100 == 0):
        print("{} is leap year".format(year))
    if(year%4==0 and year%100!=0):
        print("{} is leap year".format(year))
    else:
        print("{} is not leap year".format(year))

isLeapYear(year)