from ast import Delete
from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1140x540+210+130")
        self.root.title("employee data")
        self.root.config(bg="white")
        self.root.focus_force()
# ======Variable=======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_desc = StringVar()
        # ========searchFrame========================
        SearchFrame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=15, width=600, height=70)

        # ========option======
        lbl_search = Label(SearchFrame,text="Search By Invoice No.",bg="white",font=("times new roman", 15))
        lbl_search.place(x=10, y=10, width=180)


        text_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Times new roman", 15,), bg="white", fg="black").place(x=200, y=10, width=200)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("times new roman", 15,),bg="green", fg="white", cursor="hand2").place(x=410, y=6, width=150, height=30)

# ==================title==========

        title = Label(self.root, text="Supplier Detail", font=("goudy old style", 12, "bold"),bg="black", fg="white", bd=2, relief=RIDGE).place(x=40, y=100, width=400)

# ==========content=======
# ==================row1========
        lbl_supplier_invoice = Label(self.root, text="Supplier ID", font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=40, y=140)
        lbl_name = Label(self.root, text="Name", font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=40, y=180)
        lbl_contact = Label(self.root, text="Contact", font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=40, y=220)
        lbl_desc = Label(self.root, text="Decription", font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=40, y=260)

        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice, font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=120, y=140)
        txt_name = Entry(self.root,textvariable=self.var_name, font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=120, y=180)
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=120, y=220)
        txt_desc = Entry(self.root,textvariable=self.var_desc, font=("Times new roman", 12, "bold"), bg="white", fg="black").place(x=120, y=260)

      # ======buttons======
        btn_add = Button(self.root, text="Save", command=self.add, font=("times new roman", 15,), bg="#2196f3",fg="white", cursor="hand2").place(x=350, y=260, width=150, height=30)
        btn_update = Button(self.root, text="Update", command=self.update, font=("times new roman", 15,),bg="#4caf50", fg="white", cursor="hand2").place(x=500, y=160, width=150, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("times new roman", 15,),bg="#f44336", fg="white", cursor="hand2").place(x=500, y=210, width=150, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15,), bg="#607d8b",fg="white", cursor="hand2").place(x=500, y=260, width=150, height=30)
# =============Employee Detail========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=300, relwidth=1, height=240)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, column=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")


        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc", width=100)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

# ==========add==========================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Must Be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This supplier invoice already assigned, try diferent", parant=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Addedd Successully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

# -=======data show=========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f" due to :{str(ex)}", parent=self.root)

# =====get data======
    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_desc.set(row[3])
       
# =====update========

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "Error", "Invoice Must Be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Invoivce, try diferent", parant=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?", (

                        self.var_name.get(),                    
                        self.var_contact.get(),
                        self.var_desc.get(),                       
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Supplier Updated Successully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")
 # =============delete======

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "Error", "Invoice Must Be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Invoice, try diferent", parant=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to Delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?",
                                    (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Supplier deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")
# ======clear======

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")       
        self.var_contact.set("")
        self.var_desc.set("")
        
        self.var_searchtxt.set("")

        self.show()

# ======search=========
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice should be required", parent=self.root)
        
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found!!!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f" due to :{str(ex)}", parent=self.root)
#         
if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
