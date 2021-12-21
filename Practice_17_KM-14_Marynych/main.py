from exp_root.exponentation import exp2, exp3
from exp_root.root import root2,root3
from factorial.factorial import fact
from logarithm.logrithm import log,lg,ln
import re
c = True
def check(x):
    pattern = "[-+]?\d+(\.\d*)?|\.\d+"
    while not re.match(pattern, x) :
        x = input("Uncorrect input,try again: ")
    return float(x)
def check2(x):
    pattern = "^\d+$"
    while not re.match(pattern, x) :
        x = input("Uncorrect input,try again: ")
    return float(x)
def check3(x):
    pattern = "\d+(\.\d*)?|\.\d+"
    while not re.match(pattern, x) :
        x = input("Uncorrect input,try again: ")
    return float(x)
def check4(x):
    pattern = "^[1-9]*[.,]?[1-9]+$"
    while not re.match(pattern, x) :
        x = input("Uncorrect input,try again: ")
    return float(x)

def main():
    print('Choose program:\nEnter "1" square of number\nEnter "2" cube of number\n'
          'Enter "3" root square\nEnter "4" root cube\nEnter "5" factorial\n'
          'Enter "6" logarithm\nEnter "7" natural logarithm\nEnter "8" decimal logarithm')
    x = check(input("Type here:"))
    while True:
        if x > 8 or x < 1:
            x = check(input("There is no such program,try again:"))
        else:
            break
    if x == 1:
        a = check(input("Enter number: "))
        print('Result =',exp2(a))
    elif x == 2:
        a = check(input("Enter number: "))
        print('Result =', exp3(a))
    elif x == 3:
        a = check2(input("Enter number: "))
        print('Result =', root2(a))
    elif x == 4:
        a = check2(input("Enter number: "))
        print('Result =', root3(a))
    elif x == 5:
        a = check3(input("Enter number: "))
        print('Result =', fact(a))
    elif x == 6:
        a = check4(input("Enter base of logarithm: "))
        b = check4(input("Enter number: "))
        print('Result =', log(a,b))
    elif x == 7:
        a = check4(input("Enter number: "))
        print('Result =', lg(a))
    elif x == 8:
        a = check4(input("Enter number: "))
        print('Result =', ln(a))
while c:
    if __name__ =='__main__':
        main()
    restart = input("Do you want to restart program: 1 - Yes, 2 - No, else - No: ")
    if restart == '1' :
        continue
    else:
        print("Program finished")
        break
