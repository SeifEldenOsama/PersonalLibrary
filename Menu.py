from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import AddBook
from AddBook import Show
import RemoveBook
from RemoveBook import Show
import SearchBook
from SearchBook import Show
import displayAll 
from displayAll import Show

def AddBook1():
    AddBook.Show()

def RemoveBook1():
    RemoveBook.Show()

def SearchBook1():
    SearchBook.Show()

def DisplayAll1():
    displayAll.Show()


def Show():
    Root=Tk()
    Root.geometry("{0}x{1}+0+0".format(Root.winfo_screenwidth(),Root.winfo_screenheight())) 
    Root.configure(background="GRAY")
    Root.title("Library Menu")

    Menu=Label(Root,text="Library system",background="DARKBLUE",foreground="WHITE",font="Helvatica 50",pady=20,width=43)
    Menu.place(x=-116,y=0)

    MenuImage=Image.open(r"C://seif//library.png")
    MenuImagePhoto=ImageTk.PhotoImage(MenuImage)
    MenuLabel=Label(Root,image=MenuImagePhoto,background="DARKBLUE")
    MenuLabel.place(x=950,y=10)

    AddBookimage=Image.open(r"C://seif//addBook.png")
    AddBookimagephoto=ImageTk.PhotoImage(AddBookimage)


    AddBook=Button(Root,text="Add book",font="Helvatica 50",background="GREEN",border=11,cursor="hand2",image=AddBookimagephoto,compound="top",padx=80,command=AddBook1)
    AddBook.place(x=250,y=190)

    
    RemoveBookimage=Image.open(r"C://seif//removeBook.png")
    RemoveBookimagephoto=ImageTk.PhotoImage(RemoveBookimage)


    RemoveBook=Button(Root,text="Remove book",font="Helvatica 50",background="CRIMSON",border=10,cursor="hand2",image=RemoveBookimagephoto,compound="top",command=RemoveBook1)
    RemoveBook.place(x=800,y=190)

    
    SearchBookimage=Image.open(r"C://seif//searchBook.png")
    SearchBookimagephoto=ImageTk.PhotoImage(SearchBookimage)


    SearchBook=Button(Root,text="Search book",font="Helvatica 50",background="ORANGE",border=10,cursor="hand2",image=SearchBookimagephoto,compound="top",padx=35,command=SearchBook1)
    SearchBook.place(x=250,y=500)


    AllBookimage=Image.open(r"C://seif//allBook.png")
    AllBookimagephoto=ImageTk.PhotoImage(AllBookimage)


    AllBook=Button(Root,text="Display the entire library",font="Helvatica 31",background="YELLOW",border=10,cursor="hand2",image=AllBookimagephoto,compound="top",pady=17,padx=4,command=DisplayAll1)
    AllBook.place(x=800,y=500)

    Root.mainloop()

