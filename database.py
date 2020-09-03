from tkinter import *
import sqlite3

root = Tk()
root.title("database")
root.geometry("370x600")
com = sqlite3.connect("database")

c = com.cursor()


def show():
    global c, com

    com = sqlite3.connect("database")
    c = com.cursor()
    c.execute("INSERT INTO STUDENTS VALUES (:name, :second_name, :roll_no, :addmision_no)",

              {
                  'name': name.get(),
                  'second_name': second.get(),
                  'roll_no': roll.get(),
                  'addmision_no': add.get()
              })
    com.commit()
    com.close()
    name.delete(0, END)
    second.delete(0, END)
    roll.delete(0, END)
    add.delete(0, END)


def do():
    global com, c
    com = sqlite3.connect("database")
    c = com.cursor()
    c.execute("SELECT *,oid FROM STUDENTS")
    v = c.fetchall()
    print(v)

    pr = ""
    for recor in v:
        pr += str(recor) + "\n"
        la = Label(root, text=pr)
        la.grid(row=11, column=0, columnspan=3, padx=10, pady=10)
    com.commit()
    com.close()


d = ""


def delete():
    global com, c, d
    com = sqlite3.connect("database")
    c = com.cursor()
    d = c.execute(''' DELETE FROM STUDENTS WHERE roll_no <=0''')
    d = c.execute(''' DELETE FROM STUDENTS WHERE roll_no >=0''')
    com.commit()
    com.close()


def deleted():
    global com, c, d
    com = sqlite3.connect("database")
    c = com.cursor()
    d = c.execute(''' DELETE FROM STUDENTS WHERE oid = ''' + odd.get())
    odd.delete(0, END)
    com.commit()
    com.close()


def close():
    global com, c, od
    global name_ed, second_ed, roll_ed, add_ed
    com = sqlite3.connect("database")
    c = com.cursor()
    c.execute(''' UPDATE STUDENTS SET
           first_name = :first,
           second_name = :sed,
           roll_no = :roll,
           adimission_no = :add 
           
           WHERE oid = :oid ''',
              {
                  "first": name_ed.get(),
                  "sed": second_ed.get(),
                  "roll": roll_ed.get(),
                  "add": add_ed.get(),
                  "oid": od.get()
              })
    com.commit()
    com.close()
    od.delete(0, END)


def edi():
    global c, com, d
    edite = Tk()
    edite.title("EDIT DATA")
    edite.geometry("370x140")
    com = sqlite3.connect("database")
    c = com.cursor()
    iq = od.get()
    c.execute("SELECT * FROM STUDENTS WHERE oid = " + iq)
    d = c.fetchall()
    print(d)
    global name_ed, second_ed, roll_ed, add_ed
    name_ed = Entry(edite, width=40)
    name_ed.grid(row=0, column=1)
    second_ed = Entry(edite, width=40)
    second_ed.grid(row=1, column=1)
    roll_ed = Entry(edite, width=40)
    roll_ed.grid(row=2, column=1)
    add_ed = Entry(edite, width=40)
    add_ed.grid(row=3, column=1)
    for record in d:
        name_ed.insert(0, record[0])
        second_ed.insert(0, record[1])
        roll_ed.insert(0, record[2])
        add_ed.insert(0, record[3])
    nam_ed = Label(edite, text="   first name :    ")
    nam_ed.grid(row=0, column=0)
    sec_ed = Label(edite, text="   second name :   ")
    sec_ed.grid(row=1, column=0)
    rol_ed = Label(edite, text="   Roll no :       ")
    rol_ed.grid(row=2, column=0)
    ad_ed = Label(edite, text="    admission no :  ")
    ad_ed.grid(row=3, column=0)

    ed = Button(edite, text="ADD", command=close)
    ed.grid(row=8, column=0, columnspan=2, ipadx=160, padx=5)


name = Entry(root, width=40)
name.grid(row=0, column=1)
second = Entry(root, width=40)
second.grid(row=1, column=1)
roll = Entry(root, width=40)
roll.grid(row=2, column=1)
add = Entry(root, width=40)
add.grid(row=3, column=1)
odd = Entry(root, width=40)
odd.grid(row=7, column=1)

nam = Label(root, text="first name :")
nam.grid(row=0, column=0)
sec = Label(root, text="second name :")
sec.grid(row=1, column=0)
rol = Label(root, text="Roll no :")
rol.grid(row=2, column=0)
ad = Label(root, text="admission no :")
ad.grid(row=3, column=0)
odi = Label(root, text="id number :")
odi.grid(row=7, column=0)
but = Button(root, text="add record", command=show)
but.grid(row=4, column=0, columnspan=2, ipadx=140, padx=5)
btn = Button(root, text="show records", command=do)
btn.grid(row=5, column=0, columnspan=2, ipadx=134, padx=5)
delt = Button(root, text="delete all records", command=delete)
delt.grid(row=6, column=0, columnspan=2, ipadx=124, padx=5)
delet = Button(root, text="delete ", command=deleted)
delet.grid(row=8, column=0, columnspan=2, ipadx=151, padx=5)
edit = Button(root, text="edit data", command=edi)
edit.grid(row=10, column=0, columnspan=2, ipadx=146, padx=5)
od = Entry(root, width=40)
od.grid(row=9, column=1)
oi = Label(root, text="id number :")
oi.grid(row=9, column=0)
com.commit()
com.close()
root.mainloop()
