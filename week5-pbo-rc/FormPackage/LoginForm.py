import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class LoginForm:
    def __init__(self,window):
        self.window = window
        self.window.title("Register Form")
        self.window.minsize(300,200)
        
        self.label_username = tk.Label(window, text="Username : ")
        self.entry_username = tk.Entry(window)
        
        self.label_password = tk.Label(window,text="Password : ")
        self.entry_password = tk.Entry(window)

        self.login_button = tk.Button(window,text="Login",command=lambda: self.checkLogin(self.entry_username.get(),self.entry_password.get()))
        
        self.label_username.grid(row=0,sticky="W")
        self.label_password.grid(row=1,sticky="W")
        self.entry_username.grid(row=0,column=1,sticky="W")
        self.entry_password.grid(row=1,column=1,sticky="W")
        self.login_button.grid(row=2,column=1,sticky="W")
        
        self.username = "Mustafa"
        self.password = "123"
    
    def LoginSuccess(self):
        messagebox.showinfo("SUCCESS","Login Success !")
    def LoginFail(self):
        messagebox.showerror("FAILED","Login Failed !")
        
    def checkLogin(self,username,password):
        if username == self.username and password == self.password:
            self.LoginSuccess()
        else:
            self.LoginFail()
        
        
window = tk.Tk()
Loginform = LoginForm(window)
window.mainloop()