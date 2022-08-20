# Import Modules
from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from PIL import ImageTk, Image
import json


#----------------- LOGIN FUNCTION -----------------#

def login():
    username = username_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) ==0:
        messagebox.showerror(title="Error", message="Please make sure you haven't\nleft any fields empty")
    else:
        try:
            with open("new_users.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"No Data File Found!\nPlease register first")
            username_entry.delete(0,END)
            password_entry.delete(0,END)
            register()
        else:
            if username in data:
                if password == data[username]["password"]:
                    window.destroy()
                    login_window = Tk()
                    login_window.config(width=300, height=300)
                    login_window.title("Welcome")
                    login_window.resizable(width=False, height=False)
                    login_canvas = Canvas(login_window, width=300, height=300, highlightthickness=0)
                    bg_image_login = ImageTk.PhotoImage(Image.open("0.jpg"), master=login_window)
                    login_canvas.create_image(0,0, anchor=NW,image=bg_image_login)
                    login_canvas.create_text(150, 140,text=f"Welcome back {username},\nEviln missed you<3!",font=("Courel", 22, "italic"))
                    login_canvas.place(x=0,y=0)
                    login_window.mainloop()
                else:
                    messagebox.showerror(title="Error", message="Incorrect Password!")
                    password_entry.delete(0,END)
            else:
                messagebox.showerror(title="Error", message=f"This user {username} is not exist")


#----------------- REGISTER PAGE -----------------#

def states():
    register_button.config(state="disabled")
    login_button.config(state="disabled")

def register():
    states()
            
    def back_to_login():
        register_button.config(state="normal")
        login_button.config(state="normal")
        register_window.destroy()

    # Register function
    def register_user():
        name = name_entry.get()
        surname = surname_entry.get()
        username = username1_entry.get()
        email = email_entry.get()
        password = password1_entry.get()

        new_user = {
            username: {
                "name": name,
                "surname" : surname,
                "email": email,
                "password": password,
            }
        }

        if len(name) == 0 or len(surname) == 0 or len(username) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't\nleft any fields empty.", parent=register_window)
        else:
            try: 
                with open("new_users.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("new_users.json", "w") as data_file:
                    json.dump(new_user, data_file, indent=4)
            else:
                if username in data:
                    messagebox.showerror(title="Error", message=f"This username {username} is not available", parent=register_window)
                    username1_entry.delete(0,END)
                else:   
                    # Updating old data with new data
                    data.update(new_user)
                    with open("new_users.json", "w") as data_file:
                        # Saving new data
                        json.dump(data, data_file, indent=4)
            back_to_login()
            messagebox.showinfo(title=username, message="Register is Successful!")  
                       
    
    # Register page
    register_window = Tk()
    register_window.config(width=400, height=500)    
    register_window.title("Register")
    register_window.resizable(width=False, height=False)
    canvas_register = Canvas(register_window, width=400, height=500, highlightthickness=0)
    bg_image_register = ImageTk.PhotoImage(Image.open("0.jpg"), master=register_window)
    canvas_register.create_image(0,0, anchor=NW,image=bg_image_register)
    canvas_register.create_text(200, 50, text="REGISTER", font=("Courel", 24, "italic"))
    canvas_register.create_text(60,150 , text="Name: ", font=("Courel", 12, "bold"))
    canvas_register.create_text(60, 200, text="Surname: ", font=("Courel", 12, "bold"))
    canvas_register.create_text(60, 250, text="Username: ", font=("Courel", 12, "bold"))
    canvas_register.create_text(60, 300, text="Email: ", font=("Courel", 12, "bold"))
    canvas_register.create_text(60, 350, text="Password: ", font=("Courel", 12, "bold"))

    name_entry = Entry(register_window,width=42)
    name_entry.place(x=110, y=143)
    surname_entry = Entry(register_window,width=42)
    surname_entry.place(x=110, y=193)
    username1_entry = Entry(register_window,width=42)
    username1_entry.place(x=110, y=243)
    email_entry = Entry(register_window,width=42)
    email_entry.place(x=110, y=293)
    password1_entry = Entry(register_window,width=42, show="*")
    password1_entry.place(x=110, y=343)

    login_button1 = Button(register_window, text="BACK TO LOGIN", width=16, height=2, command=back_to_login)
    login_button1.place(x=30, y=400)

    register_button1 = Button(register_window, text="REGISTER", width=16, height=2, command=register_user)
    register_button1.place(x= 240, y=400)

    canvas_register.place(x=0,y=0)
    register_window.mainloop()
    

#----------------- MAIN PAGE -----------------#
def exit_system():
   if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()

window = Tk()
window.config(width=400, height=500)
window.title("Register and Login System")
window.resizable(width=False, height=False)
canvas = Canvas(window, width=400, height=500, highlightthickness=0)
bg_image = ImageTk.PhotoImage(Image.open("0.jpg"))
canvas.create_image(0,0, anchor=NW,image=bg_image)
canvas.create_text(210,150 , text="Hello there,\nWelcome back.", font=("Courel", 25, "italic"))
canvas.create_text(60, 290, text="Username: ", font=("Courel", 12, "bold"))
canvas.create_text(60, 345, text="Password: ", font=("Courel", 12, "bold"))
canvas.place(x=0,y=0)

username_entry = Entry(width=42)
username_entry.place(x=110, y=282)

password_entry = Entry(width=42, show="*")
password_entry.place(x=110, y=337)

login_button = Button(text="LOGIN", width=16, height=2,command=login)
login_button.place(x=30, y=400)

register_button = Button(text="REGISTER", width=16, height=2, command=register, state="normal")
register_button.place(x= 240, y=400)

window.protocol("WM_DELETE_WINDOW", exit_system)
window.mainloop()
