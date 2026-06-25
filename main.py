from tkinter import *
from tkinter import messagebox
from sys import exit
from os import remove

root = Tk()

def areyousure():
    newwindow = Toplevel()

    newwindow.title("Are You Sure?")

    yesbtn = Button(newwindow, text="Yes", width=15, height=3, fg="black", bg="green", activebackground="light green", command=exit)
    nobtn = Button(newwindow, text="No", width=15, height=3, fg="black", bg="red", activebackground="pink", command=newwindow.destroy)

    yesbtn.pack()
    nobtn.pack()

def readfunc():
    messagebox.showinfo("Read", "read")
def writefunc():
    messagebox.showinfo("Write", "write")
def createfunc():

    create_file = Toplevel()
    create_file.title("Creating a Text File")

    global input_for_name

    def confirmthename():
        filename = input_for_name.get() + ".txt"

        if filename == ".txt":
            messagebox.showinfo("Invalid Title", "The title cannot be empty")
            createfunc()

        open(filename, "x")

        create_file.destroy()

    input_for_name = Entry(create_file, width=50)
    confirm_name = Button(create_file, text="Confirm", command=confirmthename, width=25)

    input_for_name.pack()
    confirm_name.pack()

def deletefunc():
    delete_file = Toplevel()
    delete_file.title("Deleting a Text File")

    global input_for_name

    def confirmthename():
        filename = input_for_name.get() + ".txt"

        if filename == ".txt":
            messagebox.showinfo("Invalid Title", "The title cannot be empty")
            createfunc()

        remove(filename)

        delete_file.destroy()

    input_for_name = Entry(delete_file, width=50)
    confirm_name = Button(delete_file, text="Confirm Delete", command=confirmthename, width=25)

    input_for_name.pack()
    confirm_name.pack()

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