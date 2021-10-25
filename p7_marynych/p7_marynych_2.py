rgb = '#'
def  main(a):
    a = int(a)
    numbers = []
    for i in range(0,10):
        numbers.append(i)
    numbers += 'A', 'B', 'C', 'D', 'E', 'F'
    c = str(numbers[a//16])
    c += str(numbers[a%16])
    return c
def check(a):
    if a.isdigit():
        if 0 <= int(a) <= 255:
            return True
    print("Число не в інтревалі від 0 до 255!!!")
    return False
enter = "Введіть {} чилсло в інтервалі від 0 до 255: "

for i in ("перше","друге","третє"):
    while True:
        num = input(enter.format(i))
        if check(num):
            rgb += main(num).zfill(2)
            break
print(rgb)
