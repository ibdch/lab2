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
window.config(menu=menu,bg='#7B68EE')
submenu.add_command(label="Товары с наибольшим спросом", command=gonna_reg_click)
submenu.add_command(label="Динамика смены цен товара", command=gonna_reg_click)
submenu.add_command(label="Статистика улиц проживания абонентов", command=gonna_reg_click)
submenu.add_command(label="Стоимость товара по декадам", command=gonna_reg_click)
menu.add_cascade(label="Обработка данных", menu=submenu)


file_menu2 = Menu()
menu.add_cascade(label="Справка", menu=file_menu2)
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Разработчики")
file_menu2.add_command(label="Версия 1.0")
file_menu3 = Menu()
menu.add_cascade(label="Тема", menu=file_menu3)
file_menu3.add_command(label="Светлая")
file_menu3.add_command(label="Темная")


poetry = "ДОБРО ПОЖАЛОВАТЬ \n НА WILDBERRIES"
label2 = Label(text=poetry, justify=CENTER, bg="#333", fg="#eee", font='Arial 24')
label2.place(relx=.2, rely=.3)

author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.', bg='#7B68EE')
author_label.place(relx=0, rely=1, anchor='sw')

window.mainloop()