from tkinter import*
# from tkinter import __Relief
from turtle import color
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os

from matplotlib.ft2font import BOLD
from dashboard import IMS
class loginClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x670+0+0")
        self.root.title("IITM Management | Login System")
        self.root.config(bg="black")
        self.root.focus_force()
#==========================================================


#======variable========
        
        self.var_username=StringVar()
        self.var_password=StringVar()

#==================
        login_Frame=Frame(self.root,bd=3,relie=RIDGE,bg="white")
        login_Frame.place(x=300,y=100,width=800,height=500)

        txt_login=Label(login_Frame,text="Login Here",font=("goudy old style",20,"bold"),bg="black",fg="White")
        txt_login.place(x=0,y=0,relwidth=1)
#=======content=======

        lbl_username=Label(login_Frame,text="User Name",font=("Times new roman",20,"bold"),bg="white",fg="black").place(x=240,y=100)
        lbl_password=Label(login_Frame,text="Password",font=("Times new roman",20,"bold"),bg="white",fg="black").place(x=240,y=200)

        txt_username=Entry(login_Frame,textvariable=self.var_username,font=("Times new roman",20,"bold"),bg="white",fg="black").place(x=240,y=150)
        txt_password=Entry(login_Frame,textvariable=self.var_password,show="*",font=("Times new roman",20,"bold"),bg="white",fg="black").place(x=240,y=250)

        btn_login=Button(login_Frame,text="Login",command=self.login,font=("times new roman",15,),bg="#2196f3",fg="white",cursor="hand2").place(x=300,y=320,width=150,height=40)



#=========================================
    def login(self):
        if self.var_username.get()=="" or self.var_password.get()=="":
           messagebox.showerror("Error","All field Are required")
        elif self.var_username.get()!= "admin" or self.var_password.get()!="admin@123":
            
            messagebox.showerror("Error","Invalid Username or Password\n try With Correct credential")
        else:
            messagebox.showinfo("Inormation",f"Welcome : {self.var_username.get()}\nyour Password: {self.var_password.get()}")
            self.root.destroy()
            os.system("python dashboard.py")
    
   
if __name__=="__main__":
    root=Tk()
    obj=loginClass(root)
    root.mainloop()