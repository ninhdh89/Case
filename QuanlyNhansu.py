from tkinter import *
import sqlite3, sys

def connection():
    try:
        conn = sqlite3.connect("employee.db")
    except:
        print("cannot connect to the database")
    return conn


def verifier():
    a = b = c = d = e = f = 0
    if not employee_name.get():
        t1.insert(END, "<>Employee name is required<>\n")
        a = 1
    if not id.get():
        t1.insert(END, "<>ID is required<>\n")
        b = 1
    if not birth.get():
        t1.insert(END, "<>Birth is required<>\n")
        c = 1
    if not phone.get():
        t1.insert(END, "<>Phone number is requrired<>\n")
        d = 1
    if not position.get():
        t1.insert(END, "<>Position is required<>\n")
        e = 1
    if not address.get():
        t1.insert(END, "<>Address is Required<>\n")
        f = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1:
        return 1
    else:
        return 0


def add_employee():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS EMPLOYEES1(NAME TEXT,ID INTEGER,BIRTH INTEGER,PHONE_NO INTEGER,POSITION TEXT,ADDRESS TEXT)")
        cur.execute("insert into EMPLOYEES1 values(?,?,?,?,?,?)", (
        employee_name.get(), int(id.get()), birth.get(), int(phone.get()), position.get(), address.get()))
        conn.commit()
        conn.close()
        t1.insert(END, "ADDED SUCCESSFULLY\n")


def view_employee():
    conn = connection()
    cur = conn.cursor()
    cur.execute("select * from EMPLOYEES1")
    data = cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END, str(i) + "\n")


def delete_employee():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM EMPLOYEES1 WHERE ID=?", (int(id.get()),))
        conn.commit()
        conn.close()
        t1.insert(END, "SUCCESSFULLY DELETED USER\n")


def update_employee():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE EMPLOYEES1 SET NAME=?,ID=?,BIRTH=?,PHONE_NO=?,POSITION=?,ADDRESS=? where ID=?", (
        employee_name.get(), int(id.get()), birth.get(), int(phone.get()), position.get(), address.get(),int(id.get())))
        conn.commit()
        conn.close()
        t1.insert(END, "UPDATED SUCCESSFULLY !\n")


def clse():
    sys.exit()


if __name__ == "__main__":
    root = Tk()
    root.title("He thong Quan ly Nhan su")

    employee_name = StringVar()
    id = StringVar()
    birth= StringVar()
    phone = StringVar()
    position = StringVar()
    address = StringVar()

    label1 = Label(root, text="Name:")
    label1.place(x=0, y=0)

    label2 = Label(root, text="ID:")
    label2.place(x=0, y=30)

    label3 = Label(root, text="Birth:")
    label3.place(x=0, y=60)

    label4 = Label(root, text="Phone Number:")
    label4.place(x=0, y=90)

    label5 = Label(root, text="Position:")
    label5.place(x=0, y=120)

    label6 = Label(root, text="Address:")
    label6.place(x=0, y=150)

    e1 = Entry(root, textvariable=employee_name)
    e1.place(x=100, y=0)

    e2 = Entry(root, textvariable=id)
    e2.place(x=100, y=30)

    e3 = Entry(root, textvariable=birth)
    e3.place(x=100, y=60)

    e4 = Entry(root, textvariable=phone)
    e4.place(x=100, y=90)

    e5 = Entry(root, textvariable=position)
    e5.place(x=100, y=120)

    e6 = Entry(root, textvariable=address)
    e6.place(x=100, y=150)

    t1 = Text(root, width=80, height=20)
    t1.grid(row=10, column=1)

    b1 = Button(root, text="THEM NHAN SU", command=add_employee, width=40)
    b1.grid(row=11, column=0)

    b2 = Button(root, text="XEM THONG TIN", command=view_employee, width=40)
    b2.grid(row=12, column=0)

    b3 = Button(root, text="XOA", command=delete_employee, width=40)
    b3.grid(row=13, column=0)

    b4 = Button(root, text="CAP NHAT THONG TIN", command=update_employee, width=40)
    b4.grid(row=14, column=0)

    b5 = Button(root, text="THOAT", command=clse, width=40)
    b5.grid(row=15, column=0)

    root.mainloop()
