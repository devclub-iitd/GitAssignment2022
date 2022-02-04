from tkinter import *
from tkinter import messagebox

def test():  
    window=Tk()
    window.title("Pytest")
    window.geometry('500x300')
    
    t=StringVar()
    Label(window,text="Hi this is my test for Python code!").pack()
    Label(window,text="Please type any string and click on the 'Click me button'").pack()
    Entry(window,bd=10,textvariable=t).pack()
    
    def clicked():
        global a
        a=t.get()
        messagebox.showinfo("clicked","Thank You!")
        
    b=Button(window,text="Click me",command=clicked)
    b.pack()
    
    Label(window,text="Now close the pop-up window for the test to work").pack()
    window.mainloop()
    
    if type(a)==str:
        return True
    