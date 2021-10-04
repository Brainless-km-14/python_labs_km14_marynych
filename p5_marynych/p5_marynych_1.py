salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
new_salary = []
indexation = []
for i in salary_list:
    sum = (float(i) * 130) / 100
    new_salary.append(sum)
for i in range (0,7):
    ind = float(new_salary[i])- float(salary_list[i]) 
    indexation.append(round(ind,2))
for i in range (0,7):
    print("Стара заробітня плата",salary_list[i],"нова заробітня плата", new_salary[i],"сума індексації ", indexation[i])