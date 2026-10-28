students = []
grades = []

def add_student(students, grades):
    name = input("\033[32mВведите имя студента:\033[0m ").strip()
    if name == "":
        print("\033[31mОшибка: фамилия не может быть пустой.\033[0m")
    elif name in students:
        print("\033[31mОшибка: Студент уже существует!\033[0m")
    else:
        try:
            grade = int(input("\033[32mВведите оценку (от 0 до 100):\033[0m "))
            if 0 <= grade <= 100:
                students.append(name)
                grades.append(grade)
                print(f"\033[32mСтудент {name} успешно добавлен!\033[0m")
            else:
                print("\033[31mОшибка: Оценка должна быть от 0 до 100!\033[0m")
        except ValueError:
            print("\033[31mОшибка: Введено не число!\033[0m")


def show_student(students , grades):
    if len(students) == 0:
        print("\033[31mСписок студентов пуст.\033[0m")
    else:
        print("\033[32mСтуденты:\033[0m")
        for i in range(len(students)):
            print(students[i], "-", grades[i])


def find_student(students , grades):
    name = input("\033[32mВведите имя студента:\033[0m ").strip()
    if name not in students:
        print("\033[31mСтудент не найден\033[0m")
    else:
        index = students.index(name)
        print(name, "-", grades[index])


def change_grade(students, grades):
    name = input("\033[32mВведите имя студента:\033[0m ").strip()
    if name not in students:
        print("\033[31mСтудент не найден\033[0m")
    else:
        try:
            new_grade = int(input("\033[32mВведите новую оценку (от 0 до 100):\033[0m "))
            if 0 <= new_grade <= 100:
                index = students.index(name)
                grades[index] = new_grade
                print("\033[32mОценка изменена\033[0m")
            else:
                print("\033[31mОшибка: Оценка должна быть от 0 до 100!\033[0m")
        except ValueError:
            print("\033[31mОшибка: Введено не число!\033[0m")


def delete_student(students, grades):
    name = input("\033[32mВведите имя студента:\033[0m ").strip()
    if name not in students:
        print("\033[31mСтудент не найден\033[0m")
    else:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("\033[32mСтудент удалён\033[0m")


def average_score(grades):
    if len(grades) == 0:
        print("\033[31mСписок пуст, средний балл посчитать нельзя\033[0m")
    else:
        average = sum(grades) / len(grades)
        print("\033[32mСредний балл:\033[0m", average)


def menu():
    while True:
        print("""
\033[36m**************Меню программы**************\033[0m
        \033[35m1. Добавить студента
        2. Показать всех студентов
        3. Найти студента
        4. Изменить оценку
        5. Удалить студента
        6. Средний балл
        0. Выход\033[0m""")
        try:
            choice = int(input("\033[32mВыберите пункт меню:\033[0m "))
        except ValueError:
            print("\033[31mВвели не число!\033[0m")
            continue

        if choice == 1:
            add_student(students, grades)
        elif choice == 2:
            show_student(students, grades)
        elif choice == 3:
            find_student(students, grades)
        elif choice == 4:
            change_grade(students, grades)
        elif choice == 5:
            delete_student(students, grades)
        elif choice == 6:
            average_score(grades)
        elif choice == 0:
            print("Выход из программы. До свидания.")
            break
        else:
            print("Введите число от 0 до 6!!!")

menu()