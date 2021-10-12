dict = {'Newfoldland': 'A',
        'Nova Scotia': 'B',
        'Prince Edward Island': 'C',
        'New Brunswick': 'E',
        'Quebec': ('G', 'H', 'J'),
        'Ontario': ('K', 'L', 'M', 'N', 'P'),
        'Manitoba': 'R',
        'Saskatchewan': 'S',
        'Alberta': 'T',
        'British Columbia': 'V',
        'Nunavut': 'X',
        'Northwest Territories': 'X',
        'Yukon': 'Y'}
wrong_values = ['D','F', 'I',  'O' , 'Q' , 'U' , 'W' ,'Z']
index = input("Enter post index: ")
if len(index) > 3:
    print("You enter more than 3 symbols!")
else:
    a = list(index.upper())
    if a[0].isalpha() and a[1].isdigit() and a[2].isalpha():
        for n in range(len(wrong_values)):
            if a[0] == wrong_values[n]:
                print("There is no such index")
                break
        for i in dict:
            if i == "Quebec":
                for b in range(0, 3):
                    if a[0] == dict[i][b] and a[1] == '0':
                        print("User is located in a rural area", i, 'province.')
                    elif a[0] == dict[i][b] and a[1] != '0':
                        print("User is located in an urban area of", i, 'province.')
            if i == "Ontario":
                for c in range(0, 5):
                    if a[0] == dict[i][c] and a[1] == '0':
                        print("User is located in a rural area", i, 'province.')
                    elif a[0] == dict[i][c] and a[1] != '0':
                        print("User is located in an urban area of", i, 'province.')
            if a[0] == dict[i] and a[1] == '0':
                print("User is located in a rural area",i,'province.')
            elif a[0] == dict[i] and a[1] != '0':
                print("User is located in an urban area of", i, 'province.')
    else:
        print("You enter the wrong index")
