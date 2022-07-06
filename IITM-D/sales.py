from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1140x540+210+130")
        self.root.title("employee data")
        self.root.config(bg="white")
        self.root.focus_force()
#==========================================================


#======variable========
        self.bill_list=[]
        self.var_invoice=StringVar()
        
#===========tittle==============
        title=Label(self.root,text="Sales Management",font=("goudy old style",20,"bold"),bg="black",fg="white",bd=2,relief=RIDGE).place(x=10,y=20,width=1120)

#======content======
        lbl_invoice=Label(self.root,text="Invoice NO.",font=("Times new roman",15,"bold"),bg="white",fg="black").place(x=80,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("Times new roman",15,"bold"),bg="white",fg="black").place(x=200,y=100)

#=====Button=====     
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=430,y=100,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,),bg="#4caf50",fg="white",cursor="hand2").place(x=590,y=100,width=150,height=30)

#===sales frame======
        sales_Frame=Frame(self.root,bd=3,relie=RIDGE)
        sales_Frame.place(x=50,y=160,width=270,height=360)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame,font=("goudy old style",15),bg="white")
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)

        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
#=========Bill area=========

        bill_Frame=Frame(self.root,bd=3,relie=RIDGE)
        bill_Frame.place(x=330,y=160,width=420,height=360)

        lbl_title2=Label(bill_Frame,text="Customer BIll",font=("goudy old style",30),bg="black",bd=3,fg="white").pack(side=TOP,fill=X,)

        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        self.show()
#========================================================================
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(1,END)
        
        # print(os.listdir('../IMS')) bill.txt, category.py
        for i in os.listdir('bill'):
                # print(i.split('.'),i.split('.')[-1]) 
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])


    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
                messagebox.showerror("Error","Invoice no should be required",parent=self.root)
        else:
            print(self.bill_list,self.var_invoice.get())
            if self.var_invoice.get() in self.bill_list:
                # print("yes find the invoice")
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                        self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invoice No",parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)


if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()