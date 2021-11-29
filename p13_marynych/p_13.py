import string
from collections import Counter
file = open('gadsby.txt','r')
st = string.ascii_lowercase
counter = []
lines = [line.lower() for line in file]
print(lines)
for i in range (len(lines)):
    for j in range(len(lines[i])):
        for l in range(len(st)):
            if lines[i][j] == st[l]:
                    counter.append(st[l])
c = Counter(counter)
percent = []
for i in st:
    percent.append(round((c[i]*100)/len(counter),3))
letters = []
for i in st:
    letters.append(i)
dict1= dict(zip(letters,percent))
result = []
for i,j in  sorted(zip(dict1.values(),dict1.keys()))[::-1]:
    result.append(str(j)+"="+str(i))
for i in range(10):
    if i <5:
        print(result[i],"%")
    elif i >=5:
        print(result[-10+i],'%')