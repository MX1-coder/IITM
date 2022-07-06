from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1140x540+210+130")
        self.root.title("Product")
        self.root.config(bg="white")
        self.root.focus_force()
#======Variable=======
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
#=====================Product Frame===========
        product_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=500,height=500)

#title======================
        title=Label(product_Frame,text="Product Detail",font=("goudy old style",15,"bold"),bg="black",fg="white",bd=2,relief=RIDGE).pack(side=TOP,fill=X)

#content======================
        lbl_category=Label(product_Frame,text="Category",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=70)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=150)
        lbl_price=Label(product_Frame,text="Price",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=190)
        lbl_qty=Label(product_Frame,text="QYT",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=230)
        lbl_status=Label(product_Frame,text="Statuse",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=270)
        
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("times new roman",12))
        cmb_cat.place(x=140,y=70,width=165)
        cmb_cat.current(0)
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("times new roman",12))
        cmb_sup.place(x=140,y=110,width=165)
        cmb_sup.current(0)
        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=140,y=150)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=140,y=190)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=140,y=230)
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("times new roman",12))
        cmb_status.place(x=140,y=270,width=165)
        cmb_status.current(0)

#=========Button=================
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("times new roman",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=60,y=320,width=150,height=30)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("times new roman",15,),bg="#4caf50",fg="white",cursor="hand2").place(x=60,y=360,width=150,height=30)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("times new roman",15,),bg="#f44336",fg="white",cursor="hand2").place(x=250,y=320,width=150,height=30)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("times new roman",15,),bg="#607d8b",fg="white",cursor="hand2").place(x=250,y=360,width=150,height=30)
#==========Product Show==============
  #========searchFrame========================
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=530,y=10,width=590,height=70)

        #========option======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=150)
        cmb_search.current(0)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Times new roman",15,),bg="white",fg="black").place(x=170,y=10,width=230)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15,),bg="green",fg="white",cursor="hand2").place(x=420,y=6,width=150,height=30)
        
#=============Employee Detail========
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=530,y=100,width=600,height=410)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,column=("pid","category","supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("pid",text="PID")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantiy")
        self.ProductTable.heading("status",text="Status")
   
        
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=30)        
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=70)
        self.ProductTable.column("qty",width=70)
        self.ProductTable.column("status",width=100)

        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        # self.fetch_cat_sup()
#==========add==========================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")

        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:   
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                        self.cat_list.append(i[0])
                
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                        self.sup_list.append(i[0])
                
        #     print(sup)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#==========add==========================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="Select":
                messagebox.showerror("Error","All field are required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product already prasent, try diferent",parant=self.root)
                else:
                    cur.execute("Insert into product(category,supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Addedd Successully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#-=======data show=========   
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children() )
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f" due to :{str(ex)}",parent=self.root)

#=====get data======
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        # print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        
#=====update========
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","please select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parant=self.root)
                else:
                    cur.execute("Update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                                
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_pid.get()
                                        
                                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
 #=============delete======

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parant=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product deleted Successfully",parent=self.root)      
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#======clear======

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("") 
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchby.set("")
        self.var_searchtxt.set("Select")
       
        self.show()

#======search=========
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:                    
                    self.ProductTable.delete(*self.ProductTable.get_children() )
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f" due to :{str(ex)}",parent=self.root)

       


if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()
    