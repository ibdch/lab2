import tkinter as tk
from tkinter import *


def gonna_reg_click():
    window.destroy()
    import wb

def gonna_tov():
    import oks

window = tk.Tk()
window.title('WILDBERRIES')
window.geometry('600x600')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Справка', menu=file_menu)

menu = Menu(window)
submenu = Menu(window)
submenu2 = Menu(window)
window.config(menu=menu,bg='white')
submenu.add_command(label="Товары с наибольшим спросом", command=gonna_reg_click)
submenu.add_cascade(label="Динамика смены цен товара", menu=submenu2)
submenu.add_command(label="Статистика улиц проживания абонентов", command=gonna_reg_click)
submenu.add_command(label="Стоимость товара по декадам", command=gonna_reg_click)
menu.add_cascade(label="Обработка данных", menu=submenu)
submenu2.add_command(label="Кепка Puma", command=gonna_tov)
submenu2.add_command(label="Кепка North Face", command=gonna_tov)
submenu2.add_command(label="Кепка Nike", command=gonna_tov)
submenu2.add_command(label="Кепка KINZA", command=gonna_tov)

file_menu2 = Menu()
menu.add_cascade(label="Справка", menu=file_menu2)
file_menu2.add_command(label="О программе")
file_menu2.add_command(label="Разработчики")
file_menu2.add_command(label="Версия 1.0")
file_menu3 = Menu()
menu.add_cascade(label="Тема", menu=file_menu3)
file_menu3.add_command(label="Светлая")
file_menu3.add_command(label="Темная")


poetry = "ДОБРО ПОЖАЛОВАТЬ \nНА СТРАНИЦУ АДМИНИСТРАТОРА \nWILDBERRIES"
label2 = Label(text=poetry, justify=CENTER, bg="white", fg="black", font='Arial 24')
label2.place(relx=.04, rely=.3)


window.mainloop()