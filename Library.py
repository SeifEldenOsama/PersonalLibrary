import sqlite3
from tkinter import *
from tkinter import messagebox
from Book import Book1



class Library1:
    def AddBook(self,Root,Title,Author,Genre,Year):
        new_Book=Book1(Title.get(),Author.get(),Genre.get(),Year.get())
        if new_Book.getTitle()!="" and new_Book.getAuthor()!="" and new_Book.getGenre()!="" and new_Book.getYear()!="":
            try:
                Con=sqlite3.connect(r"C:\\seif\\python\\Project1\\Library.db")
                Cursor=Con.cursor()
                Cursor.execute("INSERT INTO books VALUES(?,?,?,?)",(new_Book.getTitle(),new_Book.getAuthor(),new_Book.getGenre(),int(new_Book.getYear()),))
                messagebox.showinfo("Successfully!","Book added successfully!")
                Con.commit()
                Con.close()
                self.Reset(Title,Author,Genre,Year)
                Root.deiconify()
            except Exception as e:
                print(e)   
                messagebox.showerror("Error","Unexpected error, try again!") 
                Root.deiconify()
                Con.close()
        else:
            messagebox.showerror("Error","please fill all fields!")
            Root.deiconify()

    def Reset(self,TitleEntry,AuthorEntry,GenreEntry,YearEntry):
        TitleEntry.delete(0,END)
        AuthorEntry.delete(0,END)
        GenreEntry.delete(0,END)
        YearEntry.delete(0,END)        

    def RemoveBook(self,Root,Title):
        if Title.get()!="":
            try:
                if self.IsFound(Title.get()):
                    Con=sqlite3.connect(r"C:\\seif\\python\\Project1\\Library.db")
                    Cursor=Con.cursor()
                    Cursor.execute("DELETE FROM books WHERE title=?",(Title.get(),))
                    messagebox.showinfo("successfully!","book removed successfully!")
                    Root.deiconify()
                    Con.commit()
                    Con.close()
                    Title.delete(0,END)
                else:
                    messagebox.showerror("Error","This book isn't exists!")
                    Root.deiconify()
            except Exception as e:
                print(e)
                messagebox.showerror("Error","Unexpected error, try again!")
                Root.deiconify()
                Con.close()
        else :
            messagebox.showerror("Error!","please enter book title!")
            Root.deiconify()

    def Search(self,Root,SearchList,SearchEntry):
        if SearchEntry.get()!="":
            if SearchList.get()=="Title":
                if self.IsFound(SearchEntry.get()):
                    messagebox.showinfo("found","book found!")
                    SearchEntry.delete(0,END)
                    Root.deiconify()
                else :
                    messagebox.showerror("error","book not found!")
                    Root.deiconify()
            else :
                if self.IsFound2(SearchEntry.get()):
                    messagebox.showinfo("found","book found!")
                    SearchEntry.delete(0,END)
                    Root.deiconify()
                else :
                    messagebox.showerror("error","book not found!")
                    Root.deiconify()
        else :
            messagebox.showerror("error","please fill this field!")
            Root.deiconify()



    def IsFound(self,Title):
        Con=sqlite3.connect(r"C:\\seif\\python\\Project1\\Library.db")
        Cursor=Con.cursor()
        Cursor.execute("SELECT title FROM books WHERE title=?",(Title,))
        Data=Cursor.fetchone()
        Con.commit()
        Con.close()
        if Data:
            return True 
        else :
            return False
        
    def IsFound2(self,Author):
        Con=sqlite3.connect(r"C:\\seif\\python\\Project1\\Library.db")
        Cursor=Con.cursor()
        Cursor.execute("SELECT author FROM books WHERE author=?",(Author,))
        Data=Cursor.fetchone()
        Con.commit()
        Con.close()
        if Data:
            return True 
        else :
            return False
        
    def getData(self):
        Con=sqlite3.connect(r"C:\\seif\\python\\Project1\\Library.db")
        Cursor=Con.cursor()
        Cursor.execute("SELECT * FROM books")
        Data=Cursor.fetchall()
        Con.commit()
        Con.close()
        return Data
