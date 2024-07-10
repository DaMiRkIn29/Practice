grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
average_grades = [sum(aver_grade)/len(aver_grade) for aver_grade in grades]
students_grades = {students_list[i]:average_grades[i] for i in range(len(students_list))}
print(students_grades)

# Начинается жесть по домашке))