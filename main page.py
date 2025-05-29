from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from subprocess import call
from PIL import Image, ImageTk

class RegisterApp:
    def __init__(self, root):
        self.root = root
        self.create_register_page()

    def create_register_page(self):
        label = Label(self.root, text="Registration Page")
        label.pack()

class LoginWindow:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("340x450+610+170")

        frame = Frame(self.root, bg="black")
        frame.pack(fill=BOTH, expand=True)

        get_str = Label(frame, text=title, font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host='localhost', username='root', password='d7g1@M8S2',
                                              database='management')
                cur = con.cursor()
                cur.execute("select * from login where username=%s and password=%s",
                            (self.txtuser.get(), self.txtpass.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("Success", "Welcome")
                    self.root.destroy()
                    call(['python', 'damini admin.py'])
                con.close()
            except Exception as er:
                messagebox.showerror('Error', f'Due to {str(er)}')


class LoginWindow1:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("340x450+610+170")

        frame = Frame(self.root, bg="black")
        frame.pack(fill=BOTH, expand=True)

        get_str = Label(frame, text=title, font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login1, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)

    def login1(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host='localhost', username='root', password='d7g1@M8S2',
                                              database='management')
                cur = con.cursor()
                cur.execute("select * from admin where Admin_name=%s and password=%s",
                            (self.txtuser.get(), self.txtpass.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("Success", "Welcome")
                    self.root.destroy()
                    call(['python', 'default2.py'])
                con.close()
            except Exception as er:
                messagebox.showerror('Error', f'Due to {str(er)}')


class LoginWindow3:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("340x450+610+170")

        frame = Frame(self.root, bg="black")
        frame.pack(fill=BOTH, expand=True)

        get_str = Label(frame, text=title, font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login2, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)

        registerbtn = Button(frame, text="Register", command=self.register_page, font=("times new roman", 15, "bold"),
                             bd=3, relief=RIDGE, fg="white", bg="green", activeforeground="white",
                             activebackground="green")
        registerbtn.place(x=110, y=350, width=120)

        self.entry_username = None
        self.entry_password = None

    def login2(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host='localhost', username='root', password='d7g1@M8S2',
                                              database='management')
                cur = con.cursor()
                cur.execute("select * from login where username=%s and password=%s",
                            (self.txtuser.get(), self.txtpass.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("Success", "Welcome")
                    self.root.destroy()
                    call(['python', 'user interface.py'])
                con.close()
            except Exception as er:
                messagebox.showerror('Error', f'Due to {str(er)}')

    def register_page(self):
        register_window = Toplevel(self.root)
        register_window.title("Registration Page")
        register_window.geometry("400x300")

        label = Label(register_window, text="Registration Page", font=("times new roman", 20, "bold"))
        label.pack(pady=10)

        username_label = Label(register_window, text="Username", font=("times new roman", 15, "bold"))
        username_label.pack(pady=5)

        self.entry_username = Entry(register_window, font=("times new roman", 15, "bold"))
        self.entry_username.pack(pady=5)

        password_label = Label(register_window, text="Password", font=("times new roman", 15, "bold"))
        password_label.pack(pady=5)

        self.entry_password = Entry(register_window, font=("times new roman", 15, "bold"), show="*")
        self.entry_password.pack(pady=5)

        register_button = Button(register_window, text="Register", command=self.register_user,
                                 font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                                 fg="white", bg="green", activeforeground="white", activebackground="green")
        register_button.pack(pady=10)

    def register_user(self):
        new_username = self.entry_username.get()
        new_password = self.entry_password.get()

        if not new_username or not new_password:
            messagebox.showerror("Error", "Both username and password are required for registration.")
            return

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='d7g1@M8S2', database='management')
            cur = con.cursor()

            cur.execute("SELECT * FROM login WHERE username=%s", (new_username,))
            if cur.fetchone() is not None:
                messagebox.showerror("Error", "Username already exists. Choose another one.")
                con.close()
                return

            cur.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (new_username, new_password))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration successful! You can now log in.")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed due to: {str(e)}")



class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Login Page")
        self.root.geometry("900x700+250+0")

        self.setup_ui()

    def setup_ui(self):
        Frame_login = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame_login.place(x=250, y=150, width=400, height=500)

        # Load and display image if exists
        try:
            load = Image.open("logcrime.png")
            load = load.resize((400, 400), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(Frame_login, image=render)
            img.image = render
            img.place(x=0, y=0)
        except Exception as e:
            # If image not found, just skip showing it
            pass

        btn_login_user = Button(self.root, text="User Login", command=self.open_login_user,
                                font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                                fg="white", bg="red", activeforeground="white", activebackground="red")
        btn_login_user.place(x=350, y=400, width=140)

        btn_login_admin = Button(self.root, text="Admin Login", command=self.open_login_admin,
                                 font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                                 fg="white", bg="red", activeforeground="white", activebackground="red")
        btn_login_admin.place(x=350, y=450, width=140)

        btn_login_other = Button(self.root, text="Other Login", command=self.open_login_other,
                                 font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                                 fg="white", bg="red", activeforeground="white", activebackground="red")
        btn_login_other.place(x=350, y=500, width=140)

    def open_login_user(self):
        login_window = Toplevel(self.root)
        LoginWindow(login_window, "User Login")

    def open_login_admin(self):
        login_window = Toplevel(self.root)
        LoginWindow1(login_window, "Admin Login")

    def open_login_other(self):
        login_window = Toplevel(self.root)
        LoginWindow3(login_window, "Other Login")


if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
