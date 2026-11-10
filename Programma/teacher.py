from tkinter import *
from tkinter import messagebox
from data import (load_students, save_students, sred_arif,
                  add_student, delete_student)

PER_PAGE = 10
state = {"page": 0, "typed": {}}
entries = {}


def remember():
    for login, e in entries.items():
        state["typed"][login] = e.get().strip()


def show_teacher(window, go_back):
    state["page"] = 0
    state["typed"] = {}
    draw(window, go_back)


def draw(window, go_back):
    for w in window.winfo_children():
        w.destroy()
    entries.clear()

    students = load_students()
    pages = max(1, (len(students) + PER_PAGE - 1) // PER_PAGE)
    if state["page"] >= pages:
        state["page"] = pages - 1
    start = state["page"] * PER_PAGE

    Label(window, text="Кабинет преподавателя",
          font=("Arial", 36, "bold"), fg="purple").place(x=60, y=30)
    Button(window, text="Выйти", width=10, font=("Arial", 16),
           command=go_back).place(x=1680, y=40)

    Label(window, text="Студент", font=("Arial", 20, "bold")).place(x=360, y=110)
    Label(window, text="Новая оценка", font=("Arial", 20, "bold")).place(x=800, y=110)
    Label(window, text="Средний балл", font=("Arial", 20, "bold")).place(x=1080, y=110)

    y = 170
    for s in students[start:start + PER_PAGE]:
        Button(window, text=s["name"], width=22, anchor="w",
               font=("Arial", 16),
               command=lambda s=s: show_grades(s)).place(x=360, y=y)

        e = Entry(window, width=6, font=("Arial", 20))
        e.insert(0, state["typed"].get(s["login"], ""))
        e.place(x=830, y=y)
        entries[s["login"]] = e

        Label(window, text=str(sred_arif(s["grades"])),
              font=("Arial", 20)).place(x=1130, y=y)

        Button(window, text="Удалить", font=("Arial", 14),
               command=lambda s=s: remove(window, go_back, s)).place(x=1330, y=y)
        y += 55


    Button(window, text="< Назад", width=10, font=("Arial", 14),
           command=lambda: change_page(window, go_back, -1)).place(x=360, y=760)
    Label(window, text=f"Стр. {state['page'] + 1} из {pages}",
          font=("Arial", 16)).place(x=520, y=762)
    Button(window, text="Вперёд >", width=10, font=("Arial", 14),
           command=lambda: change_page(window, go_back, 1)).place(x=700, y=760)


    Label(window, text="Новый студент:", font=("Arial", 18)).place(x=360, y=840)
    name_entry = Entry(window, width=20, font=("Arial", 20))
    name_entry.place(x=570, y=840)
    Button(window, text="Добавить", font=("Arial", 14),
           command=lambda: add(window, go_back, name_entry)).place(x=900, y=838)

    Button(window, text="Сохранить оценки", bg="purple", fg="white",
           font=("Arial", 20, "bold"), width=22,
           command=lambda: save(window, go_back)).place(x=360, y=920)


def change_page(window, go_back, step):
    remember()
    state["page"] = max(0, state["page"] + step)
    draw(window, go_back)


def show_grades(s):
    if len(s["grades"]) == 0:
        text = "Оценок пока нет"
    else:
        text = ("Оценки: " + ", ".join(str(g) for g in s["grades"]) +
                "\nСредний балл: " + str(sred_arif(s["grades"])))
    messagebox.showinfo(s["name"], text)


def save(window, go_back):
    remember()
    students = load_students()
    new = {}
    for s in students:
        text = state["typed"].get(s["login"], "")
        if text == "":
            continue
        if not text.isdigit() or not 1 <= int(text) <= 12:
            messagebox.showerror("Ошибка",
                                 f"Оценка для {s['name']} должна быть целым числом от 1 до 12!")
            return
        new[s["login"]] = int(text)

    for s in students:
        if s["login"] in new:
            s["grades"].append(new[s["login"]])
    save_students(students)
    state["typed"] = {}
    messagebox.showinfo("Готово", "Оценки сохранены!")
    draw(window, go_back)


def add(window, go_back, name_entry):
    remember()
    error = add_student(name_entry.get())
    if error:
        messagebox.showerror("Ошибка", error)
        return
    draw(window, go_back)


def remove(window, go_back, s):
    if messagebox.askyesno("Удаление", f"Удалить студента {s['name']}?"):
        remember()
        state["typed"].pop(s["login"], None)
        delete_student(s["login"])
        draw(window, go_back)