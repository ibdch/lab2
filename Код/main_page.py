import tkinter as tk
from tkinter import *
import os


path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


def gonna_reg_click():
    window.destroy()
    import wb


def gonna_click():
    window.destroy()


window = tk.Tk()
window.title('Каталог товаров')
window.geometry('600x600')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Справка', menu=file_menu)

menu = Menu(window)
submenu = Menu(window)
window.config(menu=menu,bg='#7B68EE')
submenu.add_command(label="Женское", command=gonna_reg_click)
submenu.add_command(label="Мужское", command=gonna_reg_click)
menu.add_cascade(label="Каталог товаров", menu=submenu)

file_menu4 = Menu()
menu.add_cascade(label="Информация о заказах", menu=file_menu4)
file_menu4.add_command(label="Корзина")
file_menu4.add_command(label="Оформленные заказы")

file_menu2 = Menu()
menu.add_cascade(label="Справка", menu=file_menu2)
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Разработчики")
file_menu2.add_command(label="Версия 1.0")
file_menu3 = Menu()
menu.add_cascade(label="Тема", menu=file_menu3)
file_menu3.add_command(label="Светлая")
file_menu3.add_command(label="Темная")

main_menu.add_cascade(label='Справка', menu=file_menu)

prod1_label = tk.Label(window, text='Продукт 1: Кроссовки PUMA')
prod1_label.place(x=90, y=100)

canvas1 = tk.Canvas(window, width=250, height=250, relief='solid', borderwidth=2)
canvas1.pack()
prod1_icon_file = PhotoImage(file='img/2.png')
canvas1.create_image(132, 125, image=prod1_icon_file)
canvas1.place(x=30, y=125)
gonna = tk.Button(window, text='Добавить в корзину', command=gonna_click)
gonna.place(x=90, y=400)


prod2_label = tk.Label(window, text='Продукт 2: Кроссовки NIKE AIR FORCE')
prod2_label.place(x=350, y=100)

canvas2 = tk.Canvas(window, width=251, height=251, relief='solid', borderwidth=2)
canvas2.pack()
gonna = tk.Button(window, text='Добавить в корзину', command=gonna_click)
gonna.place(x=410, y=400)

prod2_icon_file = PhotoImage(file='img/1.png')
canvas2.create_image(132, 125, image=prod2_icon_file)
canvas2.place(x=330, y=125)

gonna_reg = tk.Button(window, text='Перейти к корзине',
                      command=gonna_reg_click)
gonna_reg.place(x=240, y=450)

author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.', bg='#7B68EE')
author_label.place(relx=0, rely=1, anchor='sw')


window.mainloop()
