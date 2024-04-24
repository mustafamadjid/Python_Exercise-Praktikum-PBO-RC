import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class LoginForm:
    def __init__(self,window):
        self.window = window
        self.window.title("Register Form")
        self.window.minsize(300,200)
        
        self.username = ""
        self.password= ""
        
        self.label_username = tk.Label(window, text="Username : ")
        self.entry_username = tk.Entry(window)
        
        self.label_password = tk.Label(window,text="Password : ")
        self.entry_password = tk.Entry(window)

        self.login_button = tk.Button(window,text="Login",command=lambda: self.checkLogin(self.entry_username.get(),self.entry_password.get()))
        self.register_button = tk.Button(window,text="Registration",command=self.RegisterForm)
               
        self.label_username.grid(row=0,sticky="W")
        self.label_password.grid(row=1,sticky="W")
        self.entry_username.grid(row=0,column=1,sticky="W")
        self.entry_password.grid(row=1,column=1,sticky="W")
        self.login_button.grid(row=2,column=1,sticky="W")
        self.register_button.grid(row=3,column=1,sticky="W")
        
    
    def LoginSuccess(self):
        messagebox.showinfo("SUCCESS","Login Success !")
    def LoginFail(self):
        messagebox.showerror("FAILED","Login Failed !")
        
    def checkLogin(self,username,password):
        if self.username == "" and self.password == "":
            messagebox.showerror("FAILED","Login Failed !")
            
        elif username == self.username and password == self.password:
            self.LoginSuccess()
        else:
            self.LoginFail()
    
    def RegisterForm(self):
        register_window = tk.Toplevel()
        register_window.title('Register Form')
        register_window.minsize = (300,200)
        
        username_reg_input = tk.Label(register_window,text="Username : ")
        entry_reg_username = tk.Entry(register_window,)
        
        password_reg_input = tk.Label(register_window,text="Password : ")
        entry_reg_password = tk.Entry(register_window)
        
        reg_button = tk.Button(register_window, text="Register", command=lambda: self.registered(entry_reg_username, entry_reg_password, register_window))        
        
        username_reg_input.grid(row=0,sticky="W")
        password_reg_input.grid(row=1,sticky="W")
        entry_reg_username.grid(row=0,column=1,sticky="W")
        entry_reg_password.grid(row=1,column=1,sticky="W")
        reg_button.grid(row=2,column=1,sticky="W")
    
    def registered(self, entry_reg_username, entry_reg_password, register_window):
        # Mengambil nilai username dan password saat tombol Register ditekan
        self.username = entry_reg_username.get()
        self.password = entry_reg_password.get()
        
        if self.username == "" and self.password == "":
            messagebox.showerror("FAILED", "Registration failed, please input your data")
        else:
            messagebox.showinfo("SUCCESS", "Registration Successful!")
            register_window.destroy()
            
        
    
        
                
window = tk.Tk()
Loginform = LoginForm(window)
window.mainloop()