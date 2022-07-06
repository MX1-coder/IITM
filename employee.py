from ast import Delete
from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1140x540+210+130")
        self.root.title("employee data")
        self.root.config(bg="white")
        self.root.focus_force()
#======Variable=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_address=StringVar()
        self.var_sallary=StringVar()




        
        #========searchFrame========================
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=15,width=600,height=70)

        #========option======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Times new roman",15,),bg="white",fg="black").place(x=200,y=10,width=200)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15,),bg="green",fg="white",cursor="hand2").place(x=410,y=6,width=150,height=30)
        
#==================title==========

        title=Label(self.root,text="Employee Detail",font=("goudy old style",12,"bold"),bg="black",fg="white",bd=2,relief=RIDGE).place(x=40,y=100,width=400)

#==========content=======   
#==================row1========
        lbl_empid=Label(self.root,text="Emp ID",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=300,y=140)   
        lbl_contact=Label(self.root,text="Contact",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=570,y=140)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=100,y=140)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,text="Gender",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=360,y=140)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("times new roman",12))
        cmb_gender.place(x=380,y=140,width=165)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=650,y=140)
#==================row2========
        lbl_name=Label(self.root,text="Name",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=180)
        lbl_dob=Label(self.root,text="D.O.B",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=300,y=180)   
        lbl_doj=Label(self.root,text="D.O.J.",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=570,y=180)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=100,y=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=380,y=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=650,y=180)
#==================row3========
        lbl_email=Label(self.root,text="Email",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=220)
        lbl_pass=Label(self.root,text="Password",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=300,y=220)   
        lbl_utype=Label(self.root,text="User Type",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=570,y=220)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=100,y=220)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=380,y=220) 
        # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=600,y=220)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee","Other"),state='readonly',justify=CENTER,font=("times new roman",12))
        cmb_utype.place(x=650,y=220,width=165)
        cmb_utype.current(0)

#==================row4========
        lbl_address=Label(self.root,text="Address",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=40,y=260)
        lbl_sallary=Label(self.root,text="Sallary",font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=300,y=260)   
        

        txt_address=Entry(self.root,textvariable=self.var_address,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=100,y=260)
        txt_sallary=Entry(self.root,textvariable=self.var_sallary,font=("Times new roman",12,"bold"),bg="white",fg="black").place(x=380,y=260) 
      #======buttons======
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=650,y=260,width=150,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15,),bg="#4caf50",fg="white",cursor="hand2").place(x=870,y=160,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,),bg="#f44336",fg="white",cursor="hand2").place(x=870,y=210,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,),bg="#607d8b",fg="white",cursor="hand2").place(x=870,y=260,width=150,height=30)

#=============Employee Detail========
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=300,relwidth=1,height=240)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,column=("eid","name","email","gender","contact","dob","doj","pass","utype","address","sallary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="Utype")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("sallary",text="Sallary")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("sallary",width=100)

        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#==========add==========================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try diferent",parant=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,sallary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_emp_id.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),                                              
                                                self.var_pass.get(),
                                                self.var_utype.get(),                                                
                                                self.var_address.get(),
                                                self.var_sallary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd Successully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#-=======data show=========   
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children() )
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f" due to :{str(ex)}",parent=self.root)

#=====get data======
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])                                              
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])                                                
        self.var_address.set(row[9])
        self.var_sallary.set(row[10])
#=====update========
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, try diferent",parant=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,sallary=? where eid=?",(
                                                
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),                                              
                                                self.var_pass.get(),
                                                self.var_utype.get(),                                                
                                                self.var_address.get(),
                                                self.var_sallary.get(),
                                                self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
 #=============delete======

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, try diferent",parant=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted Successfully",parent=self.root)      
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#======clear======

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")                                              
        self.var_pass.set("")
        self.var_utype.set("Admin")                                                
        self.var_address.set("")
        self.var_sallary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        
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
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:                    
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children() )
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f" due to :{str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()
    