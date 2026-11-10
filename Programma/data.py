from json import*

def load_students():
    with open("students.json" , "r" , encoding="utf-8") as file:
        return load(file)


def save_students(students):
    with open("students.json" , "w" , encoding="utf-8") as file:
        dump(students , file)

def sred_arif(grades):
    if len(grades)==0:
        return 0
    return round (sum(grades) / len(grades) , 1)

def add_student(name):
    name = name.strip()
    if name == "":
        return "Имя не может быть пустым!"
    login = name.lower()
    if login == "sama":
        return "Логин sama занят!"
    students = load_students()
    for s in students:
        if s["login"] == login:
            return "Студент с таким логином уже есть!"
    students.append({"name": name.title(), "login": login, "grades": []})
    save_students(students)
    return


def delete_student(login):
    students = load_students()
    students = [s for s in students if s["login"] != login]
    save_students(students)