from tkinter import *

root = Tk()
root.title('Save Decks')
# root.geometry('600x400')

f_inputs = Frame(root, pady=4, padx=25)
f_inputs.pack()


def save(*args):
    n = deck_name.get()
    c = deck_code.get()
    if not n or not c:
        message_input.configure(text='Error: The fields cannot be empty', fg='red')
    else:
        message_input.configure(text='Deck saved', fg='green')

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

name_entry.focus()
root.bind('<Return>', save)

root.mainloop()
