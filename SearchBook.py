from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Library import *

def Search(Root,SearchList,SearchEntry):
    L1=Library1()
    L1.Search(Root,SearchList,SearchEntry)



def Show():
    Root=Tk() 
    Root.title("Search book")
    Root.geometry("500x350+540+180")
    Root.configure(background="ORANGE")
    
    MenuLabel=Label(Root,text="Search book",background="DARKBLUE",foreground="WHITE",width=22,pady=7,font="Helvatica 30")
    MenuLabel.place(x=0,y=0)
    
    SearchLabel=Label(Root,text="Search by :",font="Helvatica 25",background="ORANGE")
    SearchLabel.place(x=20,y=82)

    SearchEntry=Entry(Root,font="Helvatica 20",width=30,justify="center")
    SearchEntry.place(x=20,y=160)

    SearchList=ttk.Combobox(Root,values=["Title","Author"],state="readonly",font="Helvatica 15")
    SearchList.place(x=220,y=90)
    SearchList.set("Title")

    SearchButton=Button(Root,text="Search book",font="Helvatica 30",padx=100,background="YELLOW",cursor="hand2",border=6,command=lambda: Search(Root,SearchList,SearchEntry))
    SearchButton.place(x=20,y=230)

    Root.resizable(False,False)
    Root.mainloop()
