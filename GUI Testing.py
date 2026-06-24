from tkinter import *
from tkinter import messagebox
import sys

root = Tk()

def areyousure():
    newwindow = Toplevel()

    newwindow.title("Are You Sure?")

    yesbtn = Button(newwindow, text="Yes", width=15, height=3, fg="black", bg="green", activebackground="light green", command=sys.exit)
    nobtn = Button(newwindow, text="No", width=15, height=3, fg="black", bg="red", activebackground="pink", command=newwindow.destroy)

    yesbtn.pack()
    nobtn.pack()

def readfunc():
    messagebox.showinfo("Read", "read")
def writefunc():
    messagebox.showinfo("Write", "write")
def createfunc():
    messagebox.showinfo("Create", "create")
def deletefunc():
    messagebox.showinfo("Delete", "delete")

root.title("Python Text Editor")
root.geometry("1920x1080")
root.configure(bg="gray")

topframe = Frame(bg="gray")

windowtitle = Label(topframe, text="Python Text Editor", font=("Arial", 50), justify="center")
windowtitle.pack(pady=25)

Text_Input_field = Text(topframe, width="150", height="10", font=("Arial", 15), bg="white", fg="black", bd=4, yscrollcommand=True)
Text_Input_field.pack(pady=25)
topframe.pack()

bottomframe = Frame(bg="gray")

read = Button(bottomframe, text="Read", width=15, height=3, command=readfunc)
write = Button(bottomframe, text="Write", width=15, height=3, command=writefunc)
create = Button(bottomframe, text="Create", width=15, height=3, command=createfunc)
delete = Button(bottomframe, text="Delete", width=15, height=3, command=deletefunc)
exitbutton = Button(bottomframe, text="Exit", width=60, height=4, bg="red", fg="black", activebackground="blue", bd=5, command=areyousure)

bottomframe.columnconfigure(0, weight=1)
bottomframe.columnconfigure(1, weight=1)
bottomframe.columnconfigure(2, weight=1)
bottomframe.columnconfigure(3, weight=1)
bottomframe.columnconfigure(4, weight=1)
bottomframe.rowconfigure(0, weight=1)
bottomframe.rowconfigure(1, weight=1)

read.grid(row=0, column=0, sticky="e")
write.grid(row=0, column=1, sticky="e")
create.grid(row=0, column=3, sticky="w")
delete.grid(row=0, column=4, sticky="w")
exitbutton.grid(row=1, column=2, pady=25)

bottomframe.pack(pady=10)


root.mainloop()