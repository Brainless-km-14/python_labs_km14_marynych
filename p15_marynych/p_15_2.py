cards = ['A',*range(2,11),'J','D','K']
diamonds = [str(i)+' '+'diamons' for i in cards]
clubs = [str(i)+' '+'clubs' for i in cards]
hearts =[str(i)+' '+'hearts' for i in cards]
spades= [str(i)+' '+'spades' for i in cards]
deck=[]
deck +=diamonds+clubs+hearts+spades
for i in deck:
    print(i)