try:
    km = int(input(""))
    if km < 0:
        print("the speed can't be less than zero!")
    elif km >=0 and km<137:
        print("Potential damage is minor.It's not dangerous.")
    elif km >=137 and km<177:
        print("Potential damage is moderate.Be careful ")
    elif km >=177 and km<217:
        print("Potential damage is considerable.Try to not to get hurt.")
    elif km >=217 and km<266:
        print("Potential damage is severe.It's very dangerous")
    elif km >=266 and km<322:
        print("Potential damage is devastating. Try to stay alive.")
    else:
        print("Potential damage is incredible.IT'S END!")
except:
    print("Except numbers, there are other symbols!")