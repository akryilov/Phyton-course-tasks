# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

Name = ''  # Set the Name in each line
Salary = 0  # Set the Salary in each line

my_file = open('Lesson5_task3.txt', 'r')

Name_2 = []  # list of names
Salary_2 = []  # list of salary
poor_Names = []  # creating the list with names with salary lower then < 20000

for line in my_file:  # calculate the number of lines
    for name in line:
        if name == ' ':
            Name = line[0:line.index(' ')]  # Parsing the name from line untill ' ' symbol
            Name_2.append(Name)  # Write the name in list Name_2
            Salary = int(line[line.index(' '):len(line)])  # Parsing the salary from line
            Salary_2.append(Salary)  # Write the salary in list Salary_2
            Name_salary = dict(zip(Name_2, Salary_2))  # Creating the dict with key = Name, value = Salary
my_file.close()

print(f'The dictionary is: {Name_salary}')
print(f'Average salary is: {sum(Salary_2)/len(Name_2)}')  # Calculate the average salary

for key in Name_salary:  # Checking salary for the criteria
    if Name_salary.get(key) < 20000:
        poor_Names.append(key)  # Write the names with low salary in the list poor_Names
print(f'The list of persons with salary lower than 20k: {poor_Names}')
