import tkinter as tk
from tkinter import *
import os


path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


def gonna_reg_click():
    window.destroy()
    import wb


window = tk.Tk()
window.title('Основная страница')
window.geometry('600x600')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Справка', menu=file_menu)

prod1_label = tk.Label(window, text='Продукт 1: Камера')
prod1_label.place(x=100, y=100)

canvas1 = tk.Canvas(window, width=250, height=250, relief='solid', borderwidth=2)
canvas1.pack()
prod1_icon_file = PhotoImage(file='img/1.png')
canvas1.create_image(132, 125, image=prod1_icon_file)
canvas1.place(x=30, y=125)

prod2_label = tk.Label(window, text='Продукт 2: Человек тапок')
prod2_label.place(x=400, y=100)

canvas2 = tk.Canvas(window, width=251, height=251, relief='solid', borderwidth=2)
canvas2.pack()
prod2_icon_file = PhotoImage(file='img/prod2.png')
canvas2.create_image(132, 125, image=prod2_icon_file)
canvas2.place(x=330, y=125)

gonna_reg = tk.Button(window, text='Пройти регистрацию',
                      command=gonna_reg_click)
gonna_reg.place(x=225, y=450)

menu = Menu(window)
submenu = Menu(window)
window.config(menu=menu,bg='#E0ACFF')
submenu.add_command(label="Максимальный спрос", command=gonna_reg_click)
submenu.add_command(label="Динамика изменения цен", command=gonna_reg_click)
submenu.add_command(label="Список наименований улиц")
menu.add_cascade(label="Действия", menu=submenu)
menu.add_command(label="Каталог товаров")
menu.add_command(label="Корзина")

file_menu2 = Menu()
menu.add_cascade(label="Справка", menu=file_menu2)
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Разработчики")
file_menu2.add_command(label="Версия 1.0")


author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.', bg='#E0ACFF')
author_label.place(relx=0, rely=1, anchor='sw')


window.mainloop()
