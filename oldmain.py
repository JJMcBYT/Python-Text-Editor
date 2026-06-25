import os

def create_text_file():
    txtname = str(input("Please enter the name of the new text file: "))
    open(txtname + ".txt", "x")
    menu()

def display_text():
    filename = str(input("Please input the file name: "))
    f = open(filename, "r")
    print(f.read())
    f.close()
    menu()

def add_text():
    filename = str(input("Please input the file name: "))
    f = open(filename, "a")
    input_to_file = str(input("Input (raw): "))
    f.write(input_to_file)
    f.close()
    menu()

def delete_text():
    i = 0
    filename = str(input("Please input the file name: "))
    f = open(filename, "rb+")
    chars_to_remove = int(input("Please input the amount of characters to delete: "))
    f.seek((chars_to_remove // -1), 2)
    f.truncate()
    f.flush()
    f.close()
    menu()

def delete_files():
    txtname = str(input("Please enter the name of the new text file: "))
    os.remove(txtname + ".txt")
    menu()

def menu():
    global filename
    filename = ""
    print("Text Editor Options:")
    print("Important note: for options 1 and 5, do not type in the file extension as it is added in post.")
    print(
        "0 - exit\n" \
        "1 - create text file\n" \
        "2 - display file's content\n" \
        "3 - add text\n" \
        "4 - delete text\n" \
        "5 - delete files"
    )
    choice = int(input("Please input your choice: "))
    if choice == 0:
        exit(0)
    elif choice == 1:
        create_text_file()
    elif choice == 2:
        display_text()
    elif choice == 3:
        add_text()
    elif choice == 4:
        delete_text()
    elif choice == 5:
        delete_files()
    else:
        print("Unknown option, please try again")
        menu()

menu()
