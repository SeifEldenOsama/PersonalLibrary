from tkinter import *
from tkinter import messagebox
import sqlite3
from Library import Library1


def RemoveBook(Root,Title):
    L1=Library1()
    L1.RemoveBook(Root,Title)



def Show():
    Root=Tk()
    Root.title("Remove book")
    Root.geometry("500x300+540+180")
    Root.configure(background="CRIMSON")
    
    MenuLabel=Label(Root,text="Remove book",background="ORANGE",width=22,pady=7,foreground="WHITE",font="Helvatica 30")
    MenuLabel.place(x=0,y=0)

    Title=Label(Root,text="Book title :",font="Helvatica 25",background="CRIMSON")
    Title.place(x=30,y=110)

    TitleEntry=Entry(Root,font="Helvatica 15",justify="center")
    TitleEntry.place(x=200,y=120)

    RemoveButton=Button(Root,text="Remove book -",font="Helvatica 30",padx=70,background="DARKRED",cursor="hand2",border=6,command=lambda:RemoveBook(Root,TitleEntry))
    RemoveButton.place(x=30,y=190)

    Root.resizable(False,False)
    Root.mainloop()
