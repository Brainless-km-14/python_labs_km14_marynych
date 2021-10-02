try:
    age = int(input("Enter the number of years"))
    sobaka = 0
    if age < 0:
        print("The number can't be less than zero")
    else:
        for i in range(int(age)+1):
            if i > 0 and i <= 2:
                sobaka +=10.5
            elif i > 2:
                sobaka +=4
        print(age,"calendar years =",sobaka,"dog years")
except:
    print("Please enter the correct number")