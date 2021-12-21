import re
def check(pg):
    pattern = "^\d+$"
    while not re.match(pattern, pg) or int(pg) <1 or int(pg) > 1280:
        pg = input("Uncorrect input,try again: ")
    return int(pg)
pg  = check(input("Enter amount of pages : "))
while int(pg) %16 !=0:
    pg = input("Enter other amount of pages:)")
def decor(active=True):
    def wrap(func):
        def wrapper(*args, **kwargs):
            if not active:  
                b = func(*args, **kwargs)
                c =0
                for i in b:
                    c+=1
                    print(i)
                print("Notebook =",c)
            else:
                b =func(*args, **kwargs)
                z = []
                c =0
                for i in range(len(b)):
                    z.append([])
                    z[i] += [(b[i][j],b[i][j+1],b[i][j+2],b[i][j+3]) for j in range(0,len(b[i]),4)]
                for i in z:
                    c+=1
                    print(i)
                print("Notebook =",c)
        return wrapper
    return wrap
par = input("Enter argument: T = true, f = False:")
while True:
    if par.isalpha() == False:
        par = input("Please try again:")
    else:
        break
par = par.lower()

if par == "t":
    par = True     
elif par == "f":
    par = False
else:
    par = False

@decor(par)
def pages(pg):
    b =[*range(1,pg+1)]
    book =[b[i:i+16] for i in range(0, len(b), 16)]
    b =[]
    for i in range (len(book)):
        for j in range(8):
            b.append(book[i][-j+15])
            b.append(book[i][j])
    for i in range(2,len(b),4):
        b[i] , b[i+1] = b[i+1], b[i]
    book =[b[i:i+16] for i in range(0, len(b), 16)]
    return book
pages(pg)

#Головне що працює))
