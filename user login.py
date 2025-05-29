from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from subprocess import call
from PIL import Image, ImageTk

class RegisterApp:
    def __init__(self, root):
        self.root = root
        self.create_register_page()

    def create_register_page(self):
        # Add your registration page elements and logic here
        label = Label(self.root, text="Registration Page")
        label.pack()




class LoginWindow1:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("1550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text=title, font=("times new roman", 15, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        # Labels
        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login1, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)


    def login1(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost', username='root',password='d7g1@M8S2', database='management')
                cur=con.cursor() 
                cur.execute("select * from admin where Admin_name=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("successful", "Welcome") 
                    self.root.destroy()
                    call(['python','default2.py'])                  
                con.close()  
            except Exception as er:
                messagebox.showerror('error',f'Due to {str(er)}')
        
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("600x450")

        # Load background image
        image = Image.open("logcrime.png")
        image = image.resize((1550, 800), resample=Image.LANCZOS)
        background_image = ImageTk.PhotoImage(image)

        background_label = Label(self.root, image=background_image)
        background_label.image = background_image
        background_label.place(relwidth=1, relheight=1)

        # Create buttons
        button1 = ttk.Button(self.root, text="CASE FILE",command=self.open_admin_login_page_1, style="TButton")
        button1.place(relx=0.5, rely=0.35, anchor=CENTER, width=200, height=50, bordermode="outside")

        button2 = ttk.Button(self.root, text="ADMIN", command=self.open_admin_login_page_2, style="TButton")
        button2.place(relx=0.5, rely=0.5, anchor=CENTER, width=200, height=50, bordermode="outside")

        button3 = ttk.Button(self.root, text="USER", command=self.open_login_page_3, style="TButton")
        button3.place(relx=0.5, rely=0.65, anchor=CENTER, width=200, height=50, bordermode="outside")

        # Create register button
        register_button = ttk.Button(self.root, text="Register", command=self.open_register_page, style="TButton.Green")
        register_button.place(relx=0.5, rely=0.8, anchor=CENTER, width=200, height=50, bordermode="outside")

        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=10, font=("times new roman", 12, "bold"))
        style.configure("TButton.Green", background="green")
        style.configure("TButton.Red", background="red")
        style.configure("TButton.Blue", background="blue")

        # Title label configuration
        title_label = Label(self.root, text="Main Window", font=("times new roman", 24, "bold"), fg="white", bg="black")
        title_label.place(relx=0.5, rely=0.15, anchor=CENTER)

    def open_admin_login_page_1(self):
        admin_login_page_1 = Tk()
        app = LoginWindow(admin_login_page_1, "Admin Login 1")
        admin_login_page_1.mainloop()

    def open_admin_login_page_2(self):
        admin_login_page_2 = Tk()
        app = LoginWindow1(admin_login_page_2, "Admin Login 2")
        admin_login_page_2.mainloop()

    def open_login_page_3(self):
        login_page_3 = Tk()
        app = LoginWindow3(login_page_3, "User login")
        login_page_3.mainloop()

    def open_register_page(self):
        register_page = Tk()
        app = LoginWindow(register_page, "Register")
        register_page.mainloop()


class LoginWindow3:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("1550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text=title, font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        # Labels
        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
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

    def login2(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost', username='root',password='d7g1@M8S2', database='management')
                cur=con.cursor() 
                cur.execute("select * from registration where user_name=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("successful", "Welcome") 
                    self.root.destroy()
                    call(['python','user interface.py'])                  
                con.close()  
            except Exception as er:
                messagebox.showerror('error',f'Due to {str(er)}')

    def register_page(self):
        register_window = ttk.Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("400x300")

        lbl_username = Label(register_window, text="Username:", font=("times new roman", 12, "bold"))
        lbl_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = Entry(register_window, font=("times new roman", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        lbl_password = Label(register_window, text="Password:", font=("times new roman", 12, "bold"))
        lbl_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = Entry(register_window, font=("times new roman", 12), show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        register_btn = Button(register_window, text="Register", command=self.perform_registration,
                              font=("times new roman", 12, "bold"), bd=3, relief="ridge", fg="white", bg="blue",
                              activeforeground="white", activebackground="blue")
        register_btn.grid(row=2, column=1, pady=20)

    def perform_registration(self):
        new_username = self.entry_username.get()
        new_password = self.entry_password.get()

        if not new_username or not new_password:
            messagebox.showerror("Error", "Both username and password are required for registration.")
            return

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='d7g1@M8S2', database='management')
            cur = con.cursor()

        # Check if the username already exists
            cur.execute("SELECT * FROM login WHERE username=%s", (new_username,))
            existing_user = cur.fetchone()
            if existing_user:
                messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            else:
            # Insert new user into the database
                cur.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (new_username, new_password))
                con.commit()
                messagebox.showinfo("Success", "Registration successful. You can now login.")
                con.close()

        except mysql.connector.Error as er:
            messagebox.showerror('Error', f'Due to {str(er)}')
        
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    app1 = LoginWindow3(root, "Login Window")
    root.mainloop()
