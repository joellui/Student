from tkinter import *
import sqlite3 as sql
from tkinter import messagebox
import tkinter.font as tkf

root = Tk()
conn = sql.connect('Student.db')
print("Opened Database Successfully")
c = conn.cursor()

root.title("Student Details")
root.geometry("300x300+500+180")
root.configure(background="coral")

FST = tkf.Font(family="Lucida Grande", size=20)

lT = Label(root, text="Student Detail", font=FST)
lT.pack()

FSI = tkf.Font(family="Candara", size=10)

lN = Label(root, text="Name", font=FSI)
lN.pack()
eN = Entry(root)
eN.pack()

lR = Label(root, text="Roll Number", font=FSI)
lR.pack()
eR = Entry(root)
eR.pack()

lE = Label(root, text="Email", font=FSI)
lE.pack()
eE = Entry(root)
temp_e = eE.get()
eE.pack()

f = Frame(root, width=400, height=100)
f.pack(side=BOTTOM)
f.configure(background="lightblue")


def submit():
    temp_e = eE.get()
    find = temp_e.find('@')
    if find < 1:
        messagebox.showerror("Error", "Enter the correct Email")

    else:
        print("Submitted")
        n = eN.get()
        r = int(eR.get())
        e = eE.get()
        try:
            c.execute("INSERT INTO STUDENT \
              VALUES (:name, :rollno, :email)", {'name': n, 'rollno': r, 'email': e})
            conn.commit()
            messagebox.showinfo('Submission', 'Submitted Successfully !!!!')
            eN.delete(0, END)
            eR.delete(0, END)
            eE.delete(0, END)
        except:
            messagebox.showerror('Roll number', 'Already Exist')
        print(f"Name : {n}\nROll Number : {r}\nEmail : {e}")
        print(type(n), type(r), type(e))


# Submit Button
bS = Button(f, text="Submit", width=17, height=3, font=FSI, command=submit)
bS.pack(side=LEFT, padx=(5, 5), pady=(5, 5))


def check():
    print("Checking for student")
    n = eN.get()
    r = int(eR.get())
    e = eE.get()
    try:
        c.execute('select * from Student where ROLLNO = :rollno', {'rollno': r})
        temp_name = c.fetchall()
        messagebox.showerror("Already Exist", str(temp_name[0][1]) + " : : " + temp_name[0][0] + " : : " + temp_name[0][2])

    except:
        messagebox.showinfo('Roll Number', 'Good To Use')

    print(type(n), type(r), type(e))


# View Button
bC = Button(f, text="Check", width=17, height=3, font=FSI, command=check)
bC.pack(side=RIGHT, padx=(5, 5), pady=(5, 5))

root.mainloop()
conn.close()
