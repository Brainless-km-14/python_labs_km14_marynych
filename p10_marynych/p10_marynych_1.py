salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
indexation = []
new_salary = list(map(lambda i : (float(i)*130)/100,salary_list))
new_salary = list(map(lambda i: round(i,2),new_salary))
indexation = list(map(lambda i,j: float(i)-float(j),new_salary,salary_list))
indexation = list(map(lambda i: round(i,2),indexation))
print("Salary table:")
for i in range (0,7):
    print(salary_list[i] ,new_salary[i] ,indexation[i])

