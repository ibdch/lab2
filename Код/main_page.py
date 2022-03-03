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



prod1_label = tk.Label(window, text='Продукт 1')
prod1_label.place(x=128, y=100)

canvas1 = tk.Canvas(window, width=250, height=250, relief='solid', borderwidth=2)
canvas1.pack()
prod1_icon_file = PhotoImage(file='img/prod1.png')
canvas1.create_image(132, 125, image=prod1_icon_file)
canvas1.place(x=30, y=125)

prod2_label = tk.Label(window, text='Продукт 2')
prod2_label.place(x=428, y=100)

canvas2 = tk.Canvas(window, width=250, height=250, relief='solid', borderwidth=2)
canvas2.pack()
prod2_icon_file = PhotoImage(file='img/prod1.png')
canvas2.create_image(132, 125, image=prod2_icon_file)
canvas2.place(x=330, y=125)

gonna_reg = tk.Button(window, text='Пройти регистрацию',
                      command=gonna_reg_click)
gonna_reg.place(x=225, y=450)

gonna_kat = tk.Button(window, text='Каталог товаров',
                      command=gonna_reg_click)
gonna_kat.place(x=0, y=0)

gonna_max = tk.Button(window, text='Max спрос',
                      command=gonna_reg_click)
gonna_max.place(x=0, y=0)

gonna_din = tk.Button(window, text='Динамика изменения цен',
                      command=gonna_reg_click)
gonna_din.place(x=0, y=0)

gonna_kor = tk.Button(window, text='Корзина',
                      command=gonna_reg_click)
gonna_kor.place(x=0, y=0)

gonna_spr = tk.Button(window, text='Справка',
                      command=gonna_reg_click)
gonna_spr.place(x=540, y=0)

author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.')
author_label.place(relx=0, rely=1, anchor='sw')


window.mainloop()
