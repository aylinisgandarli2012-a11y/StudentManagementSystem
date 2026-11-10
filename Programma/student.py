from tkinter import *
from data import sred_arif


def show_student(window, s, go_back):
    for w in window.winfo_children():
        w.destroy()

    Label(window, text="Кабинет студента", font=("Arial", 36, "bold"),
          fg="purple").place(x=60, y=30)
    Button(window, text="Выйти", width=10, font=("Arial", 16),
           command=go_back).place(x=1680, y=40)

    Label(window, text=s["name"], font=("Arial", 48, "bold")).place(x=360, y=200)

    if len(s["grades"]) == 0:
        Label(window, text="Оценок пока нет",
              font=("Arial", 28)).place(x=360, y=340)
    else:
        grades = ", ".join(str(g) for g in s["grades"])
        Label(window, text="Оценки: " + grades, font=("Arial", 28)).place(x=360, y=340)
        Label(window, text="Средний балл: " + str(sred_arif(s["grades"])),
              font=("Arial", 32, "bold")).place(x=360, y=520)