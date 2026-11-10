from tkinter import *
from PIL import Image , ImageTk
from  data import load_students
from tkinter import messagebox
from teacher import show_teacher
from student import show_student

window = Tk()
window.geometry("1920x1080")
window.resizable(False, False)
window.iconbitmap("m.ico")
window.title("MyStat")

def back_to_login():
    for w in window.winfo_children():
        w.destroy()
    show_registor()

def login():
    name = login_entry.get()
    password = password_entry.get()

    if name == "sama" and password == "teacher2017":
        print("Страница учителя открыта")
        messagebox.showinfo("Вход выполнен успешно!" , "Здраствуйте , Cяма!")
        show_teacher(window, back_to_login)
        return

    students = load_students()
    for student in students:
        if name == student["login"]:
            if password == "123" + name:
                print("Страница студента открыта")
                messagebox.showinfo("Вход выполнен успешно", f"Здраствуйте , {name.title()}!")
                show_student(window, student, back_to_login)
                return

    messagebox.showerror("Неудачный вход!" , "Неверное имя пользователя или пароль!")



def show_registor():
    global photo , login_entry , password_entry

    image = Image.open("praviyfon.png")
    image = image.resize((1054,1080))
    photo = ImageTk.PhotoImage(image)
    foto = Label(window , image=photo)
    foto.place(x = 855, y = 0)


    mystat = Label(window , text = "MyStat" , fg = "purple" , font=( "Arial" , 30 , "bold"))
    mystat.place(x =20 , y =20)

    login_label = Label(window , text = "Login" , fg = "black" , font=( "Arial" , 20 , "bold"))
    login_label.place(x =430 , y =380)

    login_entry = Entry(window , fg = "gray" , width = 20 , font=( "Arial" , 25 , "bold"))
    login_entry.place(x =300 , y =450)

    login_label = Label(window, text="Password", fg="black", font=("Arial", 20, "bold"))
    login_label.place(x=430, y=500)

    password_entry = Entry(window , fg = "gray" , width = 20 , font=( "Arial" , 25 , "bold") , show="*")
    password_entry.place(x =300 , y =550)

    login_btn = Button(window , text = "Login" , bg = "purple" , fg = "white" , width = 18 , font=( "Arial" , 25 , "bold") , command=login )
    login_btn.place(x =300 , y =650 )


show_registor()
mainloop()