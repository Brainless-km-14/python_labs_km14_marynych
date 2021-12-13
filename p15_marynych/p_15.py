import re
def check(a):
    pattern = "^\d+$"
    while not re.match(pattern, a):
        a = input("Uncorrect input, try again: ")
    return int(a)
n = check(input("Enter degree: "))
row =[1]
print(*row)
for i in range(n):
    f_row =[1]
    if i ==0:
        f_row+=row
        row =f_row
    else:
        f_row +=[row[i]+row[i+1] for i in range(len(row)-1)]
        f_row +=[1]
        row =f_row
    print(*row)
