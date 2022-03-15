import tkinter as tk
from tkinter import *


def gonna_reg_click():
    window.destroy()
    import wb


window = tk.Tk()
window.title('WILDBERRIES')
window.geometry('600x600')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Справка', menu=file_menu)

menu = Menu(window)
submenu = Menu(window)
window.config(menu=menu,bg='white')
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

l2 = Label(text='Оформленные заказы', font='Arial 18', fg='black', bg='white')
l2.place(relx=.3, rely=.0)

l1 = Label(text =' № ЗАКАЗА: \n Наименование товара: \n Цена за единицу: \n Количество: \n Общая стоимость:', justify=LEFT, bg='white', font='Arial 12')
l1.place(relx=.0, rely=.1)

l3 = Label(text=' Дата заказа: \n Время заказа:', font='Arial 12', fg='black', bg='white', justify=LEFT)
l3.place(relx=.0, rely=.8)
l4 = Label(text=' Итоговая сумма:', font='Arial 12', fg='black', bg='white', justify=LEFT)
l4.place(relx=.5, rely=.8)

author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.', bg='white')
author_label.place(relx=0, rely=1, anchor='sw')

window.mainloop()