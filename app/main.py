import webbrowser
from tkinter import *
from tkinter import filedialog

from app.db_csv import save_deck
from app.db_csv import update_custom_path
from app.project_version import get_version


root = Tk()
root.title('Save Decks')
# root.geometry('600x400')

f_inputs = Frame(root, pady=4, padx=25)
f_inputs.pack()

# Get version of the project
VERSION = get_version()


def save(*args):
    n = deck_name.get()
    c = deck_code.get()
    if not n or not c:
        message_input.configure(text='Error: The fields cannot be empty', fg='red')
        return

    try:
        save_deck(name=n, code=c)
        message_input.configure(text='Deck saved', fg='green')
    except Exception as e:
        print(e)
        message_input.configure(text='Error: something went wrong.', fg='red')
        
    print(n)
    print(c)
    deck_name.set('')
    deck_code.set('')
    

deck_name = StringVar()
name_entry = Entry(f_inputs, textvariable=deck_name)
name_entry.grid(row=0, column=1)

deck_code = StringVar()
code_entry = Entry(f_inputs, textvariable=deck_code)
code_entry.grid(row=1, column=1)


Label(f_inputs, text='Deck name:').grid(row=0, column=0, pady=5)
Label(f_inputs, text='Code:').grid(row=1, column=0, pady=5)


btn_save = Button(f_inputs, text='Save', bg="#35d735" ,command=save)
btn_save.grid(row=2,column=0, columnspan=2, sticky='nswe', pady=10)

message_input = Label(f_inputs, text='',)
message_input.grid(row=3, columnspan=2, column=0, sticky='nswe')


# Menus
root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root['menu'] = menubar

menu_config = Menu(menubar)
menu_about = Menu(menubar)
menubar.add_cascade(menu=menu_config, label='Config')


def interface_about():
    def open_web():
        webbrowser.open('https://github.com/Harold875/save-decks')
    
    t = Toplevel()
    t.title("About")
    t.resizable(False, False)
    
    f = Frame(t, padx=30, pady=20)
    f.grid(row=0, column=0, sticky="nsew")
    f.columnconfigure(0, weight=1)

    lbl_version = Label(f, text=f"Version {VERSION}", font=("TkDefaultFont", 10))
    lbl_version.grid(row=0, column=0, pady=(0, 15), sticky="ew")

    btn_web = Button(
        f,
        text="View on GitHub",
        command=open_web,
        cursor="hand2",
        padx=10,
        pady=3
    )
    btn_web.grid(row=1, column=0, sticky="ew")


menubar.add_command(label='About', command=interface_about)


def change_path_file():
    dirname = filedialog.askdirectory()
    if dirname:
        print(dirname)
        update_custom_path(dirname)
        print("cambiar ruta...")
    else:
        print('Empty...')
    

menu_config.add_command(label='Change save path', command=change_path_file)



name_entry.focus()
root.bind('<Return>', save)

root.mainloop()
