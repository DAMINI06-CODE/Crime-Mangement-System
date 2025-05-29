from multiprocessing.sharedctypes import Value
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x850+0+0')
        self.root.title("CRIME RECORD MANAGEMENT SYSTEM")


        self.var_caseID = StringVar()
        self.var_Criminal_no = StringVar()
        self.var_Name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()


        lbl_title = Label(self.root, text="CRIME RECORD MANAGEMENT SYSTEM SOFTWERE", font=('times new roman',40,'bold'), bg='black',fg='gold')
        lbl_title.place(x=0, y=0, width=1530,height=70)

        # img_logo = Image.open('ncrb.jpg')
        # img_logo = img_logo.resize((60, 60), Image.ANTIALIAS)
        # self.photo_logo = ImageTk.PhotoImage(img_logo)

        # self.logo = Label(self.root, image = self.photo_logo)
        # self.logo.place(x = 80, y = 5, width = 60, height = 60)


        img_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'White')
        img_frame.place(x = 0, y = 70, width=1530, height=130)

        img1 = Image.open('crime1.png')
        img1 = img1.resize((540, 160), resample=Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image = self.photo1)
        self.img_1.place(x = 0, y = 0, width = 540, height = 160)


        img2 = Image.open('C.png')
        img2 = img2.resize((540, 160), resample=Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image = self.photo2)
        self.img_2.place(x = 540, y = 0, width = 540, height = 160)


        img3 = Image.open('crime38.png')
        img3 = img3.resize((540, 160), resample=Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image = self.photo3)
        self.img_3.place(x = 1080, y = 0, width = 540, height = 160)


        main_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'White')
        main_frame.place(x = 10, y=200, width =1500, height=560)

        upper_frame = LabelFrame(main_frame,  text="Criminal Information", font=('times new roman',12,'bold'), bg='White',fg='red')
        upper_frame.place(x = 10, y=10, width =1480, height=270)


        caseid = Label(upper_frame, text='Case ID: ', font='arial 11 bold', bg='white')
        caseid.grid(row=0, column=0, padx=5, sticky=W)

        case_entry = ttk.Entry(upper_frame,textvariable=self.var_caseID, width=22, font='arial 11 bold')
        case_entry.grid(row=0, column=1, padx=5,pady=7, sticky=W)


        lbl_criminal_no = Label(upper_frame, text='Criminal NO: ', font='arial 11 bold', bg='white')
        lbl_criminal_no.grid(row=0, column=2, padx=7, sticky=W)

        txt_criminal_no = ttk.Entry(upper_frame,textvariable=self.var_Criminal_no, width=22, font='arial 11 bold')
        txt_criminal_no.grid(row=0, column=3, padx=7, sticky=W)


        lbl_Name = Label(upper_frame, text='Criminal Name: ', font='arial 11 bold', bg='white')
        lbl_Name.grid(row=1, column=0, padx=5,pady=7, sticky=W)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_Name, width=22, font='arial 11 bold')
        txt_name.grid(row=1, column=1, padx=5,pady=7, sticky=W)


        lbl_nickname = Label(upper_frame, text='NickName: ', font='arial 11 bold', bg='white')
        lbl_nickname.grid(row=1, column=2, padx=5,pady=7, sticky=W)

        txt_nickname = ttk.Entry(upper_frame,textvariable=self.var_nickname, width=22, font='arial 11 bold')
        txt_nickname.grid(row=1, column=3, padx=5,pady=7, sticky=W)


        lbl_arrestDate = Label(upper_frame, text='Arrest Date: ', font='arial 11 bold', bg='white')
        lbl_arrestDate.grid(row=2, column=0, padx=5,pady=7, sticky=W)

        txt_arrestDate = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font='arial 11 bold')
        txt_arrestDate.grid(row=2, column=1, padx=5,pady=7, sticky=W)


        lbl_dateOfCrime = Label(upper_frame, text='Date of Crime: ', font='arial 11 bold', bg='white')
        lbl_dateOfCrime.grid(row=2, column=2, padx=5,pady=7, sticky=W)

        txt_dateOfCrime = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font='arial 11 bold')
        txt_dateOfCrime.grid(row=2, column=3, padx=5,pady=7, sticky=W)


        lbl_address = Label(upper_frame, text='Address: ', font='arial 11 bold', bg='white')
        lbl_address.grid(row=3, column=0, padx=5,pady=7, sticky=W)

        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font='arial 11 bold')
        txt_address.grid(row=3, column=1, padx=5,pady=7, sticky=W)


        lbl_age = Label(upper_frame, text='Age: ', font='arial 11 bold', bg='white')
        lbl_age.grid(row=3, column=2, padx=5,pady=7, sticky=W)

        txt_age = ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font='arial 11 bold')
        txt_age.grid(row=3, column=3, padx=5,pady=7, sticky=W)


        lbl_occupation = Label(upper_frame, text='Occupation: ', font='arial 11 bold', bg='white')
        lbl_occupation.grid(row=4, column=0, padx=5,pady=7, sticky=W)

        txt_occupation = ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font='arial 11 bold')
        txt_occupation.grid(row=4, column=1, padx=5,pady=7, sticky=W)


        lbl_birthMark = Label(upper_frame, text='Birth Mark: ', font='arial 11 bold', bg='white')
        lbl_birthMark.grid(row=4, column=2, padx=5,pady=7, sticky=W)

        txt_birthMark = ttk.Entry(upper_frame,textvariable=self.var_birthMark, width=22, font='arial 11 bold')
        txt_birthMark.grid(row=4, column=3, padx=5,pady=7, sticky=W)


        lbl_crimeType = Label(upper_frame, text='Crime Type: ', font='arial 11 bold', bg='white')
        lbl_crimeType.grid(row=0, column=4, padx=5,pady=7, sticky=W)

        txt_crimeType = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font='arial 11 bold')
        txt_crimeType.grid(row=0, column=5, padx=5,pady=7, sticky=W)


        lbl_fatherName = Label(upper_frame, text='Father Name: ', font='arial 11 bold', bg='white')
        lbl_fatherName.grid(row=1, column=4, padx=5,pady=7, sticky=W)

        txt_fatherName = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font='arial 11 bold')
        txt_fatherName.grid(row=1, column=5, padx=5,pady=7, sticky=W)


        lbl_gender = Label(upper_frame, text='Gender: ', font='arial 11 bold', bg='white')
        lbl_gender.grid(row=2, column=4, padx=5,pady=7, sticky=W)

        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=755, y=90, width=180, height=30)

        male = Radiobutton(radio_frame_gender, text='Male',variable=self.var_gender, value='male', font='arial 9 bold')
        male.grid(row=0, column=0, pady=2, padx=10, sticky=W)

        female = Radiobutton(radio_frame_gender, text='Female',variable=self.var_gender, value='female', font='arial 9 bold')
        female.grid(row=0, column=1, pady=2, padx=10, sticky=W)


        lbl_wanted = Label(upper_frame, text='Most Wanted: ', font='arial 11 bold', bg='white')
        lbl_wanted.grid(row=3, column=4, padx=5,pady=7, sticky=W)

        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=755, y=130, width=180, height=30)

        yes = Radiobutton(radio_frame_wanted, text='Yes',variable=self.var_wanted, value='yes', font='arial 9 bold')
        yes.grid(row=0, column=0, pady=2, padx=10, sticky=W)

        no = Radiobutton(radio_frame_wanted, text='No',variable=self.var_wanted, value='no', font='arial 9 bold')
        no.grid(row=0, column=1, pady=2, padx=10, sticky=W)


        Button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        Button_frame.place(x=5, y=200, width=620, height=45)

        btn_add = Button(Button_frame,command=self.add_data, text='Record Save', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)


        btn_clear = Button(Button_frame,command=self.clear_data, text='Clear', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=2, padx=3, pady=5)


        img4 = Image.open('crime31.png')
        img4 = img4.resize((470, 245), resample=Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(upper_frame, image = self.photo4)
        self.img_4.place(x = 1000, y = 0, width = 470, height = 245)




        

    def add_data(self):
        if self.var_caseID.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password = 'd7g1@M8S2', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into criminal values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)', (self.var_caseID.get(),
                                                                                                                    self.var_Criminal_no.get(),
                                                                                                                    self.var_Name.get(),
                                                                                                                    self.var_nickname.get(),
                                                                                                                    self.var_arrest_date.get(),
                                                                                                                    self.var_date_of_crime.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_age.get(),
                                                                                                                    self.var_occupation.get(),
                                                                                                                    self.var_birthMark.get(),
                                                                                                                    self.var_crime_type.get(),
                                                                                                                    self.var_father_name.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_wanted.get()))
                conn.commit()
                self.clear_data()
                conn.close()                      
                messagebox.showinfo('Success', 'Criminal record has been added')
            
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')
    
    
    
    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']
        self.var_caseID.set(data[0])
        self.var_Criminal_no.set(data[1])
        self.var_Name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])



    def clear_data(self):
        self.var_caseID.set("")
        self.var_Criminal_no.set("")
        self.var_Name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")


    def search_data(self):
        if self.var_com_search.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password = 'd7g1@M8S2', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" like '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')



if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
