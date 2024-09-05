from tkinter import *
from tkinter import ttk 
from Library import *




def Show():
    Root=Tk() 
    Root.title("the entire library")
    Root.geometry("700x700+350+30")

    style = ttk.Style(Root)
    style.configure("Treeview", background="ORANGE", foreground="black")
    style.configure("Treeview.Heading", background="BLUE", foreground="black")

    table=ttk.Treeview(Root,height=33,style="Treeview")
    table.place(x=0,y=0)
    table["columns"]=("Title","Author","Genre","Publication year")
    table.column("#0", width=35,anchor="center")
    table.column("Title", width=200,anchor="center")
    table.column("Author", width=200,anchor="center")
    table.column("Genre", width=150,anchor="center")
    table.column("Publication year", width=120,anchor="center")
    table.heading("#0", text="")
    table.heading("Title", text="Title")
    table.heading("Author", text="Author")
    table.heading("Genre", text="Genre")
    table.heading("Publication year", text="Year")
    
    L1=Library1()
    Data=L1.getData() 

    for i, book in enumerate(Data, start=1):
        table.insert("", "end", iid=i, text=str(i), values=book)
    



    Root.resizable(False,False)
    Root.mainloop() 

