from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import Menu
from Menu import Show


def SignIn1(username,password):
    if username=="admin" and password=="123":
        messagebox.showinfo("successfully!","signed in successfully!")
        Root.destroy()
        Menu.Show()
    else:
        messagebox.showerror("error","username or password error!")




Root=Tk()
Root.geometry("300x300+550+150")
Root.configure(background="DARKCYAN")
Root.title("Sign in")

SignIn=Label(Root,text="SIGN IN",font="Helvatica 25",background="DARKCYAN")
SignIn.place(x=90,y=15)

userimage=Image.open(r"C:\seif\SignIn.png")
userimagephoto=ImageTk.PhotoImage(userimage)
userimagelabel=Label(Root,image=userimagephoto,background="DARKCYAN")
userimagelabel.place(x=30,y=87)

userentry=Entry(Root,width=15,font="Hevatica 15", borderwidth=5, relief="solid", border=5,justify="center")
userentry.place(x=100,y=97)

passimage=Image.open(r"C:\seif\pass.png")
passimagephoto=ImageTk.PhotoImage(passimage)
passimagelabel=Label(Root,image=passimagephoto,background="DARKCYAN")
passimagelabel.place(x=30,y=170)

passentry=Entry(Root,width=15,font="Hevatica 15", borderwidth=5, relief="solid", border=5,show="*",justify="center")
passentry.place(x=100,y=180)


signin=Button(Root,text="SIGN IN",width=21,font="Helvatica 15",background="DARKGREEN",cursor="hand2",border=5,command=lambda:SignIn1(userentry.get(),passentry.get()))
signin.place(x=35,y=235)

Root.resizable(False,False)
Root.mainloop()