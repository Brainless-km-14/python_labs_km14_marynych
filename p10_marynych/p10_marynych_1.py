import numpy as np
month = input("Enter the month: ")
while True:
    if len(month)>2 or len(month)<1 or month.isdigit() == False or int(month)>12 or int(month)<1:
                print("You entered the wrong month, please try again")
                month = input("Enter the month: ")
    else:
        break
year = input("Enter the year: ")
while True:
    if len(year)!=4 or month.isdigit() == False or int(year)>2023 or int(year)<1900:
                print("You entered the wrong year, please try again")
                year = input("Enter the year: ")
    else:
        break
years = np.arange(1900, 2020+3, 1)
#print(years)
days= [31,29,31,30,31,30,31,31,30,31,30,31]
def a(years):
    l  = list(filter(lambda i : i%400 ==0,years))
    l2 = list(filter(lambda i : i%400 !=0,years))
    l3 = list(filter(lambda i : i%100 !=0,l2))
    l4 = list(filter(lambda i : i%4 ==0,l3))
    l +=l4
    return l

def b(x,y,function):
    if int(y) in function(years):
        days[1]= 28
    elif int(y) not in function(years):
        days[1]=29
    print("In the year",year,"in month",month,days[int(x)-1],"days")
b(month,year,a)
    