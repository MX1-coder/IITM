from msilib.schema import File
from tkinter import*
from tkinter.font import BOLD
from PIL import Image,ImageTk
from employee  import employeeClass
from category  import categoryClass
from product  import productClass
from supplier  import supplierClass
from sales  import salesClass
import sqlite3
import os
from tkinter import messagebox
import time
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("IITM management system")
        self.root.config(bg="white")
        
        #variable---
        # self.primary="black"
        # self.secondary="white"

#=======title====================================================================
        # self.icon_title=PhotoImage(file="images/logo.png")image=self.icon_title,compound=LEFT,
        title=Label(self.root,text="IITM management System",font=('times new roman',40,"bold"),bg="black",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

#=======LogoutButton===========================================================
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=('times new roman',15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

#==clock============================================================================
        self.lbl_clock=Label(self.root,text="Welcome to IITM management system\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=('times new roman',15,),bg="white",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

#===========LEft Menu===================================================================
        self.MenuLogo=Image.open("images/menu.jpeg")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)


        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP ,fill=X)

        # self.icon_side=PhotoImage(file="images/employee.png")image=self.icon_side,compound=LEFT,padx=20,
        lbl_menu=Label(LeftMenu,text="Menu",font=('times new roman',20),bg="Black",fg="white").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,font=('times new roman',20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)

#====contant==============================================

        self.lbl_employee=Label(self.root,text="Total Employee\n [ 0 ]",bd=2,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=280,y=120,height=100,width=200)
        
        self.lbl_category=Label(self.root,text="Total category\n [ 0 ]",bd=2,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=480,y=120,height=100,width=200)
        
        self.lbl_product=Label(self.root,text="Total product\n [ 0 ]",bd=2,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=680,y=120,height=100,width=200)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]",bd=2,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=880,y=120,height=100,width=200)
        
        self.lbl_sales=Label(self.root,text="Total sales\n [ 0 ]",bd=2,relief=RIDGE,bg="black",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=1080,y=120,height=100,width=200)

        graph_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white",graph=plt.show())
        graph_frame.place(x=205,y=230,height=430,width=1140)

        self.lbl_graph=Label(graph_frame,text="Graph",bd=1,relief=RIDGE,bg="green",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_graph.place(x=5,y=5,width=100)
        btn_graph=Button(graph_frame,text="Graph",command=self.graph,font=('times new roman',20,"bold"),bg="green",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)

 #==Footer=================================================================
        lbl_footer=Label(self.root,text="IITM management system for any Technical ishu contact us",font=('times new roman',15,),bg="black",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()
        self.graph()
#===================Content Update================================= 
    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')
   
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total suppliers\n[ {str(len(supplier))} ]')
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total categorys\n[ {str(len(category))} ]')
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total employees\n[ {str(len(employee))} ]')

            cur.execute("SELECT SUM(price) as sum_price FROM product")
            sum_price=cur.fetchall()
            self.lbl_sales.config(text=f'Total sales\n{sum_price}')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To IITM Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
                                  
        except Exception as ex:
            messagebox.showerror(
                "Error", f" due to :{str(ex)}", parent=self.root)
#=============Graph=================   
    def graph(self):  
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        cur.execute("select name, price from product")
        data=cur.fetchall

        names=[]
        prices=[]
        for i in cur:
            names.append(i[0])
            prices.append(i[1])

        # print("Name of product = ", names)
        # print("Price of Products = ", prices)
        # data = {
        #     'Python': 11.27,
        #     'C': 11.16,
        #     'Java': 10.46,
        #     'C++': 7.5,
        #     'C#': 5.26
        #                         }
        # languages = data.keys()
        # popularity = data.values()
        figure = Figure(figsize=(6, 4), dpi=100)

        figure_canvas = FigureCanvasTkAgg(figure, self.root)
        # NavigationToolbar2Tk(figure_canvas, self.root)
        # create axes
        axes = figure.add_subplot()
        # create the barchart
        axes.bar(names, prices)
        axes.set_title('Top Sales')
        axes.set_ylabel('Amount')
        figure_canvas.get_tk_widget().place(x=220,y=300, height=300)


        # con = sqlite3.connect(database=r'ims.db')
        # cur = con.cursor()
        # cur.execute("select name, price from product")
        # data=cur.fetchall

        # names=[]
        # prices=[]
        # for i in cur:
        #     names.append(i[0])
        #     prices.append(i[1])

        # # print("Name of product = ", names)
        # # print("Price of Products = ", prices)    
        # plt.bar(names, prices)
        # plt.ylim(0,5)
        # plt.xlabel("Name")
        # plt.ylabel("Amount ")
        # plt.title("sale's Information")
        # plt.show() 
#=======================root callllss================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def exit(self):
        self.root.destroy()

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()