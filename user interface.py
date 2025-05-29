import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

class RegisterPage(tk.Toplevel):
    def __init__(self, parent, login_page):
        super().__init__(parent)
        self.login_page = login_page

        self.title("Register Page")
        self.geometry("400x300")

        # Load a background image using PIL
        img = Image.open("hands.png")
        background_image = ImageTk.PhotoImage(img)
        background_label = tk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a transparent overlay with a canvas
        canvas = tk.Canvas(self, bg="", highlightthickness=0)
        canvas.place(relwidth=1, relheight=1)

        # Create widgets for the register page
        label = tk.Label(canvas, text="Register Page", font=("Helvetica", 20, "bold"), fg="#333")
        label.pack(pady=10)

        # Centered frame for entry widgets
        entry_frame = tk.Frame(canvas, bg="rgba(0, 0, 0, 0)")
        entry_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        username_label = tk.Label(entry_frame, text="Enter Name:", font=("italics", 14), fg="#fff")
        username_label.pack(pady=5)

        self.username_entry = ttk.Entry(entry_frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        password_label = tk.Label(entry_frame, text="Password:", font=("courier New", 14), fg="#fff")
        password_label.pack(pady=5)

        self.password_entry = ttk.Entry(entry_frame, show="*", font=("courier New", 12))
        self.password_entry.pack(pady=5)

        # Create a themed button with a more creative style
        style = ttk.Style()
        style.configure("Fetch.TButton", font=("Comic Sans MS", 14), foreground="#fff", background="#4CAF50", padding=(10, 5))
        register_button = ttk.Button(entry_frame, text="Register", command=self.register, style="Fetch.TButton")
        register_button.pack(pady=15)

    def register(self):
        # Get username and password from the entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Implement registration logic here (customize as needed)
        print(f"Registered User: {username}, Password: {password}")

        # Call the login method in the parent login page to log in the user after registration
        self.login_page.login(username, password)
        # Close the register page
        self.destroy()

def fetch_details():
    # Get the entered name from the entry widget
    name = entry_name.get()

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="d7g1@M8S2",
        database="management"
    )
    
    cursor = connection.cursor()

    # Query to fetch details based on the entered name
    query = f"SELECT * FROM criminal WHERE Criminal_Name = '{name}'"

    cursor.execute(query)
    result = cursor.fetchone()

    # Display the details in the labels
    if result:
        details_label.config(text=f"Criminal Name: {result[3]}\nCaseId: {result[0]}\nCrimeNo: {result[2]}\nArrestDate: {result[4]}\nCrimeofDate: {result[5]}\nCrimeType:{result[10]}\n Gender:{result[12]}\nWanted:{result[13]}", fg="#333", bg="white")
    else:
        details_label.config(text="No details found for the given name", fg="#333", bg="white")

    # Close database connection
    cursor.close()
    connection.close()

# Create the main window
root = tk.Tk()
root.title("Crime Management System")

# Load a background image for the main window using PIL
img_main = Image.open("hands.png")
background_image_main = ImageTk.PhotoImage(img_main)
background_label_main = tk.Label(root, image=background_image_main)
background_label_main.place(relwidth=1, relheight=1)

# Configure style for Fetch button (themed button)
style = ttk.Style()
style.configure("Fetch.TButton", font=("Comic Sans MS", 14), foreground="#fff", background="#FF5722", padding=(10, 5))

# Create and place widgets
label_name = tk.Label(root, text="Enter Name:", font=("Helvetica", 16), fg="#fff", bg="black")
label_name.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

entry_name = tk.Entry(root, font=("Helvetica", 14))
entry_name.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

fetch_button = ttk.Button(root, text="Fetch Details", command=fetch_details, style="Fetch.TButton")
fetch_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

details_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#fff", bg="black")
details_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# Run the main loop
root.mainloop()
