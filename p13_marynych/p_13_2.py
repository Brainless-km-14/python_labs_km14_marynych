from collections import Counter
files = []
for i in range(1880, 2020):
    files.append("yob" + str(i) + ".txt")
l = []
namesM=[]
namesF=[]
for i in files:
    file = open(i,'r')
    sex = []
    lines = file.readlines()
    for line in lines:
        l.append(line.split(","))
    for j in range(len(l)):
        if l[j][1] not in sex and l[j][1] == "M":
            sex.append(l[j][1])
            namesM.append(l[j][0])
        if l[j][1] not in sex and l[j][1] == "F":
            sex.append(l[j][1])
            namesF.append(l[j][0])
        if "F" and "M" in sex:
            l=[]
            break
c1 = Counter(namesM)
c2 = Counter(namesF)
new_namesF=set(namesF)
new_namesM=set(namesM)
for i in new_namesM:
    print(i, c1[i])
print("..................")
for i in new_namesF:
    print(i, c2[i])