from tkinter import *
from tkinter import messagebox
import sqlite3
from Library import Library1


def AddBook(Root,Title,Author,Genre,Year):
    L1=Library1()
    L1.AddBook(Root,Title,Author,Genre,Year)


def Show():
    Root=Tk()
    Root.title("Add Book")
    Root.geometry("600x600+510+70")
    Root.configure(background="GREEN")
    
    MenuLabel=Label(Root,text="Add book",background="CRIMSON",foreground="WHITE",width=26,font="Helvatica 30",pady=10)
    MenuLabel.place(x=0,y=0)

    
    Name=Label(Root,text="Book title :",font="Helvatica 25",background="GREEN")
    Name.place(x=50,y=120)

    NameEntry=Entry(Root,font="Helvatica 15")
    NameEntry.place(x=300,y=130)

    Author=Label(Root,text="Book author :",font="Helvatica 25",background="GREEN")
    Author.place(x=50,y=210)

    AuthorEntry=Entry(Root,font="Helvatica 15")
    AuthorEntry.place(x=300,y=220)


    Genre=Label(Root,text="Book genre :",font="Helvatica 25",background="GREEN")
    Genre.place(x=50,y=300)

    GenreEntry=Entry(Root,font="Helvatica 15")
    GenreEntry.place(x=300,y=310)


    Year=Label(Root,text="Public year :",font="Helvatica 25",background="GREEN")
    Year.place(x=50,y=390)

    YearEntry=Entry(Root,font="Helvatica 15")
    YearEntry.place(x=300,y=400)

    AddButton=Button(Root,text="Add book +",font="Helvatica 30",padx=125,cursor="hand2",background="DARKGREEN",border=6,command=lambda: AddBook(Root,NameEntry,AuthorEntry,GenreEntry,YearEntry))
    AddButton.place(x=50,y=480)

    Root.resizable(False,False)
    Root.mainloop()
