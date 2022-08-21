from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os

compiler = Tk()
compiler.title('PyCode V 0.0.5')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code before running.')
        text.pack()
        return
        
    code = editor.get("1.0", END)
    exec(code)

def clear():
    os.system("CLS")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

term_bar = Menu(menu_bar, tearoff=0)
term_bar.add_command(label='Clear', command=clear)
menu_bar.add_cascade(label='Terminal', menu=term_bar)

compiler.config(menu=menu_bar)

editor = Text(bg="#232323", font="Consolas", foreground="white", insertbackground="white")
editor.pack()

compiler.mainloop()
