rgb = '#'
numbers = [0,1,2,3,4,5,6,7,8,9,'A', 'B', 'C', 'D', 'E', 'F']
enter = "Введіть {} чилсло в інтервалі від 0 до 255: "
for i in ("перше", "друге", "третє"):
    while True:
        num = input(enter.format(i))
        if num.isdigit():
            if 0 <= int(num) <= 255:
                answ = str(numbers[int(num) // 16]) + str(numbers[int(num) % 16])
                rgb += answ.zfill(2)
                break
            else:
                print("Число не в інтревалі від 0 до 255!!!")
        else:
            print("Ви ввели недопустиме значення!!!")
print(rgb)
