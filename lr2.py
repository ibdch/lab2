from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def del_text():
    answer = mb.askokcancel('Удаление текста', 'Реально удалить?')
    if answer:
        text.delete(1.0, END)


def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
    except (FileNotFoundError, TypeError):
        mb.showinfo("Открытие файла", "Файл не выбран!")
    else:
        s = f.read()
        text.insert(1.0, s)
        f.close()


def extract_text():
    file_name = fd.asksaveasfilename()
    try:
        f = open(file_name, 'w')
    except (FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла", "Файл не сохранен!")
    else:
        s = text.get(1.0, END)
        f.write(s)
        f.close()


root = Tk()

mainmenu = Menu()
root['menu'] = mainmenu
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

file_menu2 = Menu()
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Разработчики")
file_menu2.add_command(label="Версия 1.0")

mainmenu.add_cascade(label="File", menu=file_menu)
mainmenu.add_command(label="Открыть", command=insert_text)
mainmenu.add_command(label="Сохранить", command=extract_text)
mainmenu.add_cascade(label="Справка", menu=file_menu2)
text = Text(width=50, height=25)
text.pack()

popupmenu = Menu(text, tearoff=0)
popupmenu.add_command(label="Очистить", command=del_text)

text.bind('<Button-3>',
          lambda event: popupmenu.post(event.x_root, event.y_root))

root.mainloop()
