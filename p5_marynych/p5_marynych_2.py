print ("enter n when stop ")
g = True
list = []
ad = "and"
while g:
    a = input("")
    list.append(a)
    if  a == "n":
        g = False
list.remove("n") 
if len(list)>1:
    list.insert(-1,"and")
length = len(list) 
for i in range(length):
    if i >= int(length)- 3:
        print(list[i], end = " ")
    else: 
        print(list[i], end = ",")
