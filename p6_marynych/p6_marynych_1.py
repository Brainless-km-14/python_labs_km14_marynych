ph1 = input("Введіть прешу фразу: ")
ph2 = input("Введіть другу фразу: ")
a = ph1.replace(' ','')
b = ph2.replace(' ','')
if a.isalpha() and b.isalpha:
    t1  = set(a.lower())
    t2  = set(b.lower())
    interscetion = t1 & t2
    if interscetion == t2: 
        print("Множина літер першої фрази: ",t1 )
        print("Множина літер другої фрази: ",t2 )
        print("З першої фрази можна зробити другу!")
    if interscetion != t2: 
        print("З першої фрази НЕ можна зробити другу!")
else:
    print("В фразах є не тільки букви!")
