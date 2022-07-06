from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1140x540+210+130")
        self.root.title("Category")
        self.root.config(bg="white")
        self.root.focus_force()
#======Variable=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cat_id=StringVar()
        self.var_name=StringVar()

       
#==================title==========

        title=Label(self.root,text="Category Management",font=("goudy old style",20,"bold"),bg="black",fg="white",bd=2,relief=RIDGE).place(x=10,y=20,width=1120)

#==========content=======   
#==================row1========
        lbl_name=Label(self.root,text="Category Name",font=("Times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Times new roman",15,"bold"),bg="white",fg="black").place(x=200,y=100)
   
       #======buttons=====
        btn_add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=40,y=150,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,),bg="#f44336",fg="white",cursor="hand2").place(x=200,y=150,width=150,height=30)

#=============Category Detail========
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=40,y=200,width=400,height=300)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,column=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        
        self.CategoryTable.heading("cid",text="CID")
        self.CategoryTable.heading("cid",text="Category Name")
       
        
        self.CategoryTable["show"]="headings"

        self.CategoryTable.column("cid",width=90)
        self.CategoryTable.column("name",width=100)
     
        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#====================================
# ==========add==========================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Must Be required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This  Category already assigned, try diferent", parant=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)", (
                        self.var_name.get(),
                        
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Categoryr Addedd Successully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


# -=======data show=========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f" due to :{str(ex)}", parent=self.root)

# =====get data===  ===
    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
  
# =============delete======

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror(
                    "Error", "Please select category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",
                            (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Error Please try again", parant=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to Delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?",
                                    (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Category deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")
# ======clear======





if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()
    