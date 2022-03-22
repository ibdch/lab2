import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter.ttk as ttk
import sys

def black():
    window.config(bg='black')
    poetry = "ДОБРО ПОЖАЛОВАТЬ \nНА СТРАНИЦУ АДМИНИСТРАТОРА \nWILDBERRIES"
    label2 = Label(text=poetry, justify=CENTER, bg="black", fg="white", font='Arial 24')
    label2.place(relx=.04, rely=.3)

def white():
    window.config(bg='white')
    poetry = "ДОБРО ПОЖАЛОВАТЬ \nНА СТРАНИЦУ АДМИНИСТРАТОРА \nWILDBERRIES"
    label2 = Label(text=poetry, justify=CENTER, bg="white", fg="black", font='Arial 24')
    label2.place(relx=.04, rely=.3)

def knz(u):
    data = pd.read_csv('knz.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    data = data.sort_values(u, ascending=False)
    a = data[:5]
    x = a['Товар'].to_numpy()
    y = a[u].to_numpy()
    fig, ax = plt.subplots()

    color_rectangle = np.random.rand(7, 3)  # RGB
    ax.bar(x, y, color=color_rectangle, width=0.5)

    color_rectangle = np.random.rand(7, 4)  # RGBA
    color_rectangle[:, 3] = 0.5

    ax.bar(x, y, color=color_rectangle)
    ax.set_title('Товары с наибольшим спросом')
    ax.set_xlabel('Товар')  # название для оси X
    ax.set_ylabel('Спрос')  # название для оси Y

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)

    plt.show()


def jan():
    knz('Спрос за январь')


def feb():
    knz('Спрос за февраль')


def march():
    knz('Спрос за март')


def april():
    knz('Спрос за апрель')


def may():
    knz('Спрос за май')


def june():
    knz('Спрос за июнь')


def july():
    knz('Спрос за июль')


def august():
    knz('Спрос за август')


def sept():
    knz('Спрос за сентябрь')


def oct():
    knz('Спрос за октябрь')


def novem():
    knz('Спрос за ноябрь')


def december():
    knz('Спрос за декабрь')


def eug1():
    df = pd.read_csv('eug.csv')
    country_data = df["Адрес"]
    medal_data = df["Количество"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#2ca02c", "#d62728"]
    explode = (0.1, 0, 0, 0, 0, 0, 0)
    plt.pie(medal_data, labels=country_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True,
            startangle=140)
    plt.title("Наименование улиц \n" + "на которых проживают абоненты предприятия")
    plt.show()


def gonna_tov():
    data = pd.read_csv('oks.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Дата'].to_numpy()
    y = data['Кепка Puma'].to_numpy()
    plt.figure(figsize=(16, 6))
    plt.xlabel('Дата')
    plt.ylabel('Стоимость')
    plt.title('Динамика изменения цен товара Кепка Puma')
    plt.plot(x, y)
    plt.show()


def gonna_tov1():
    data = pd.read_csv('oks.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Дата'].to_numpy()
    y = data['Кепка North Face'].to_numpy()
    plt.figure(figsize=(16, 6))
    plt.xlabel('Дата')
    plt.ylabel('Стоимость')
    plt.title('Динамика изменения цен товара North Face')
    plt.plot(x, y)
    plt.show()


def gonna_tov2():
    data = pd.read_csv('oks.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Дата'].to_numpy()
    y = data['Кепка Nike'].to_numpy()
    plt.figure(figsize=(16, 6))
    plt.xlabel('Дата')
    plt.ylabel('Стоимость')
    plt.title('Динамика изменения цен товара Кепка Nike')
    plt.plot(x, y)
    plt.show()


def gonna_tov3():
    data = pd.read_csv('oks.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Дата'].to_numpy()
    y = data['Кепка KINZA'].to_numpy()
    plt.figure(figsize=(16, 6))
    plt.xlabel('Дата')
    plt.ylabel('Стоимость')
    plt.title('Динамика изменения цен товара Кепка KINZA')
    plt.plot(x, y)
    plt.show()


def dec(v):
    data = pd.read_csv('dec1.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Кепка'].to_numpy()
    y = data[v].to_numpy()
    # даем название осям и графику
    plt.xlabel('Цена')
    plt.ylabel('Товар')
    plt.title('Стоимость по декадам')
    # Используем Matplotlib, чтобы нарисовать линейную диаграмму
    plt.barh(x, y, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')
    plt.show()


def decc(b):
    data = pd.read_csv('dec2.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Кепка'].to_numpy()
    y = data[b].to_numpy()
    # даем название осям и графику
    plt.xlabel('Цена')
    plt.ylabel('Товар')
    plt.title('Стоимость по декадам')
    # Используем Matplotlib, чтобы нарисовать линейную диаграмму
    plt.barh(x, y, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')
    plt.show()


def deccc(v):
    data = pd.read_csv('dec3.csv', sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')
    x = data['Кепка'].to_numpy()
    y = data[v].to_numpy()
    # даем название осям и графику
    plt.xlabel('Цена')
    plt.ylabel('Товар')
    plt.title('Стоимость по декадам')
    # Используем Matplotlib, чтобы нарисовать линейную диаграмму
    plt.barh(x, y, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')
    plt.show()


def dec1():
    dec('Стоимость 1 декады')


def dec2():
    dec('Стоимость 2 декады')


def dec3():
    dec('Стоимость 3 декады')


def dec4():
    dec('Стоимость 4 декады')


def dec5():
    dec('Стоимость 5 декады')


def dec6():
    dec('Стоимость 6 декады')


def dec7():
    dec('Стоимость 7 декады')


def dec8():
    dec('Стоимость 8 декады')


def dec9():
    dec('Стоимость 9 декады')


def dec10():
    dec('Стоимость 10 декады')


def dec11():
    dec('Стоимость 11 декады')


def dec12():
    dec('Стоимость 12 декады')


def decc1():
    decc('Стоимость 1 декады')


def decc2():
    decc('Стоимость 2 декады')


def decc3():
    decc('Стоимость 3 декады')


def decc4():
    decc('Стоимость 4 декады')


def decc5():
    decc('Стоимость 5 декады')


def decc6():
    decc('Стоимость 6 декады')


def decc7():
    decc('Стоимость 7 декады')


def decc8():
    decc('Стоимость 8 декады')


def decc9():
    decc('Стоимость 9 декады')


def decc10():
    decc('Стоимость 10 декады')


def decc11():
    decc('Стоимость 11 декады')


def decc12():
    decc('Стоимость 12 декады')


def deccc1():
    deccc('Стоимость 1 декады')


def deccc2():
    deccc('Стоимость 2 декады')


def deccc3():
    deccc('Стоимость 3 декады')


def deccc4():
    deccc('Стоимость 4 декады')


def deccc5():
    deccc('Стоимость 5 декады')


def deccc6():
    deccc('Стоимость 6 декады')


def deccc7():
    deccc('Стоимость 7 декады')


def deccc8():
    deccc('Стоимость 8 декады')


def deccc9():
    deccc('Стоимость 9 декады')


def deccc10():
    deccc('Стоимость 10 декады')


def deccc11():
    deccc('Стоимость 11 декады')


def deccc12():
    deccc('Стоимость 12 декады')


def spr1():
    def main(*args):
        '''Main entry point for the application.'''
        global root
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        # Creates a toplevel widget.
        global _top1, _w1
        _top1 = root
        _w1 = Toplevel1(_top1)
        root.mainloop()

    class Toplevel1:
        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.', background=_bgcolor)
            self.style.configure('.', foreground=_fgcolor)
            self.style.configure('.', font="TkDefaultFont")
            self.style.map('.', background=
            [('selected', _compcolor), ('active', _ana2color)])

            top.geometry("462x224+570+177")
            top.minsize(120, 1)
            top.maxsize(1711, 1048)
            top.resizable(1, 1)
            top.title("О программе")
            top.configure(background="#d9d9d9")

            self.top = top

            self.TLabel1 = ttk.Label(self.top)
            self.TLabel1.place(relx=0.022, rely=-0.022, height=29, width=459)
            self.TLabel1.configure(background="#d9d9d9")
            self.TLabel1.configure(foreground="#000000")
            self.TLabel1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel1.configure(relief="flat")
            self.TLabel1.configure(anchor='w')
            self.TLabel1.configure(justify='left')
            self.TLabel1.configure(text='''Автоматизированная информационная система Wildberries''')
            self.TLabel1.configure(compound='left')

            self.TLabel2 = ttk.Label(self.top)
            self.TLabel2.place(relx=0.022, rely=0.103, height=26, width=435)
            self.TLabel2.configure(background="#d9d9d9")
            self.TLabel2.configure(foreground="#000000")
            self.TLabel2.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2.configure(relief="flat")
            self.TLabel2.configure(anchor='w')
            self.TLabel2.configure(justify='left')
            self.TLabel2.configure(text='''предназначена для оформления заказов пользователей,''')
            self.TLabel2.configure(compound='left')

            self.TLabel2_1 = ttk.Label(self.top)
            self.TLabel2_1.place(relx=0.022, rely=0.223, height=26, width=435)
            self.TLabel2_1.configure(background="#d9d9d9")
            self.TLabel2_1.configure(foreground="#000000")
            self.TLabel2_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1.configure(relief="flat")
            self.TLabel2_1.configure(anchor='w')
            self.TLabel2_1.configure(justify='left')
            self.TLabel2_1.configure(text='''обработки данных о пользователях и заказах.''')
            self.TLabel2_1.configure(compound='left')

            self.TLabel2_1_1 = ttk.Label(self.top)
            self.TLabel2_1_1.place(relx=0.022, rely=0.357, height=26, width=435)
            self.TLabel2_1_1.configure(background="#d9d9d9")
            self.TLabel2_1_1.configure(foreground="#000000")
            self.TLabel2_1_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1_1.configure(relief="flat")
            self.TLabel2_1_1.configure(anchor='w')
            self.TLabel2_1_1.configure(justify='left')
            self.TLabel2_1_1.configure(text='''Обработка данных включает в себя:''')
            self.TLabel2_1_1.configure(compound='left')

            self.TLabel2_1_1_1 = ttk.Label(self.top)
            self.TLabel2_1_1_1.place(relx=0.022, rely=0.446, height=37, width=435)
            self.TLabel2_1_1_1.configure(background="#d9d9d9")
            self.TLabel2_1_1_1.configure(foreground="#000000")
            self.TLabel2_1_1_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1_1_1.configure(relief="flat")
            self.TLabel2_1_1_1.configure(anchor='w')
            self.TLabel2_1_1_1.configure(justify='left')
            self.TLabel2_1_1_1.configure(text='''1. Аналитику спроса на товары''')
            self.TLabel2_1_1_1.configure(compound='left')

            self.TLabel2_1_1_1_1 = ttk.Label(self.top)
            self.TLabel2_1_1_1_1.place(relx=0.022, rely=0.58, height=36, width=435)
            self.TLabel2_1_1_1_1.configure(background="#d9d9d9")
            self.TLabel2_1_1_1_1.configure(foreground="#000000")
            self.TLabel2_1_1_1_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1_1_1_1.configure(relief="flat")
            self.TLabel2_1_1_1_1.configure(anchor='w')
            self.TLabel2_1_1_1_1.configure(justify='left')
            self.TLabel2_1_1_1_1.configure(text='''2. Динамику изменения цен''')
            self.TLabel2_1_1_1_1.configure(compound='left')

            self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
            top.configure(menu=self.menubar)

            self.TLabel2_1_1_1_1_1 = ttk.Label(self.top)
            self.TLabel2_1_1_1_1_1.place(relx=0.022, rely=0.714, height=38
                                         , width=435)
            self.TLabel2_1_1_1_1_1.configure(background="#d9d9d9")
            self.TLabel2_1_1_1_1_1.configure(foreground="#000000")
            self.TLabel2_1_1_1_1_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1_1_1_1_1.configure(relief="flat")
            self.TLabel2_1_1_1_1_1.configure(anchor='w')
            self.TLabel2_1_1_1_1_1.configure(justify='left')
            self.TLabel2_1_1_1_1_1.configure(text='''3. Статистику улиц  доставки товаров''')
            self.TLabel2_1_1_1_1_1.configure(compound='left')
            self.TLabel2_1_1_1_1_1.configure(cursor="fleur")

            self.TLabel2_1_1_1_1_1_1 = ttk.Label(self.top)
            self.TLabel2_1_1_1_1_1_1.place(relx=0.022, rely=0.848, height=27
                                           , width=435)
            self.TLabel2_1_1_1_1_1_1.configure(background="#d9d9d9")
            self.TLabel2_1_1_1_1_1_1.configure(foreground="#000000")
            self.TLabel2_1_1_1_1_1_1.configure(font="-family {Segoe UI} -size 12")
            self.TLabel2_1_1_1_1_1_1.configure(relief="flat")
            self.TLabel2_1_1_1_1_1_1.configure(anchor='w')
            self.TLabel2_1_1_1_1_1_1.configure(justify='left')
            self.TLabel2_1_1_1_1_1_1.configure(text='''4. Статистику стоимости товаров по декадам''')
            self.TLabel2_1_1_1_1_1_1.configure(compound='left')

    if __name__ == '__main__':
        main()

def spr2():
    def main(*args):
        '''Main entry point for the application.'''
        global root
        root = tk.Tk()
        root.protocol('WM_DELETE_WINDOW', root.destroy)
        # Creates a toplevel widget.
        global _top1, _w1
        _top1 = root
        _w1 = Toplevel1(_top1)
        root.mainloop()

    class Toplevel1:
        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'

            top.geometry("388x224+553+205")
            top.minsize(120, 1)
            top.maxsize(1711, 1048)
            top.resizable(1, 1)
            top.title("Разработчики")
            top.configure(background="#d9d9d9")

            self.top = top

            self.Label1 = tk.Label(self.top)
            self.Label1.place(relx=0.018, rely=0.022, height=36, width=287)
            self.Label1.configure(anchor='w')
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(compound='left')
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 12")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='''В разработке проекта участвовали:''')

            self.Label2 = tk.Label(self.top)
            self.Label2.place(relx=0.026, rely=0.188, height=21, width=226)
            self.Label2.configure(anchor='w')
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(compound='left')
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 12")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(text='''Бурханов Руслан''')

            self.Label3 = tk.Label(self.top)
            self.Label3.place(relx=0.026, rely=0.281, height=21, width=120)
            self.Label3.configure(anchor='w')
            self.Label3.configure(background="#d9d9d9")
            self.Label3.configure(compound='left')
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 12")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(text='''Вагина Оксана''')

            self.Label4 = tk.Label(self.top)
            self.Label4.place(relx=0.026, rely=0.375, height=21, width=158)
            self.Label4.configure(anchor='w')
            self.Label4.configure(background="#d9d9d9")
            self.Label4.configure(compound='left')
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font="-family {Segoe UI} -size 12")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(text='''Кушманов Евгений''')

            self.Label5 = tk.Label(self.top)
            self.Label5.place(relx=0.026, rely=0.469, height=21, width=139)
            self.Label5.configure(anchor='w')
            self.Label5.configure(background="#d9d9d9")
            self.Label5.configure(compound='left')
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(font="-family {Segoe UI} -size 12")
            self.Label5.configure(foreground="#000000")
            self.Label5.configure(text='''Серикова Дарья''')

    if __name__ == '__main__':
        main()

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
submenu3 = Menu(window)
submenu4 = Menu(window)
submenu5 = Menu(window)
submenu6 = Menu(window)
submenu7 = Menu(window)
window.config(menu=menu, bg='white')
submenu.add_cascade(label="Товары с наибольшим спросом", menu=submenu3)
submenu.add_cascade(label="Динамика смены цен товара", menu=submenu2)
submenu.add_command(label="Статистика улиц проживания абонентов", command=eug1)
submenu.add_cascade(label="Стоимость товара по декадам", menu=submenu4)
submenu4.add_cascade(label='Первые 12 декад (статистика за первые 4 месяца)', menu=submenu5)
submenu5.add_command(label='1 декада', command=dec1)
submenu5.add_command(label='2 декада', command=dec2)
submenu5.add_command(label='3 декада', command=dec3)
submenu5.add_command(label='4 декада', command=dec4)
submenu5.add_command(label='5 декада', command=dec5)
submenu5.add_command(label='6 декада', command=dec6)
submenu5.add_command(label='7 декада', command=dec7)
submenu5.add_command(label='8 декада', command=dec8)
submenu5.add_command(label='9 декада', command=dec9)
submenu5.add_command(label='10 декада', command=dec10)
submenu5.add_command(label='11 декада', command=dec11)
submenu5.add_command(label='12 декада', command=dec12)
submenu4.add_cascade(label='Вторые 12 декад (статистика за 4-8 месяцы)', menu=submenu6)
submenu6.add_command(label='1 декада', command=decc1)
submenu6.add_command(label='2 декада', command=decc2)
submenu6.add_command(label='3 декада', command=decc3)
submenu6.add_command(label='4 декада', command=decc4)
submenu6.add_command(label='5 декада', command=decc5)
submenu6.add_command(label='6 декада', command=decc6)
submenu6.add_command(label='7 декада', command=decc7)
submenu6.add_command(label='8 декада', command=decc8)
submenu6.add_command(label='9 декада', command=decc9)
submenu6.add_command(label='10 декада', command=decc10)
submenu6.add_command(label='11 декада', command=decc11)
submenu6.add_command(label='12 декада', command=decc12)
submenu4.add_cascade(label='Третьи 12 декад (статистика за 8-12 месяцы)', menu=submenu7)
submenu7.add_command(label='1 декада', command=deccc1)
submenu7.add_command(label='2 декада', command=deccc2)
submenu7.add_command(label='3 декада', command=deccc3)
submenu7.add_command(label='4 декада', command=deccc4)
submenu7.add_command(label='5 декада', command=deccc5)
submenu7.add_command(label='6 декада', command=deccc6)
submenu7.add_command(label='7 декада', command=deccc7)
submenu7.add_command(label='8 декада', command=deccc8)
submenu7.add_command(label='9 декада', command=deccc9)
submenu7.add_command(label='10 декада', command=deccc10)
submenu7.add_command(label='11 декада', command=deccc11)
submenu7.add_command(label='12 декада', command=deccc12)
menu.add_cascade(label="Обработка данных", menu=submenu)
submenu2.add_command(label="Кепка Puma", command=gonna_tov)
submenu2.add_command(label="Кепка North Face", command=gonna_tov1)
submenu2.add_command(label="Кепка Nike", command=gonna_tov2)
submenu2.add_command(label="Кепка KINZA", command=gonna_tov3)
submenu2.add_command(label="Кепка LAOCHRA", command=gonna_tov3)
submenu2.add_command(label="Кепка AKSANIII", command=gonna_tov3)
submenu2.add_command(label="Кепка KAMARR", command=gonna_tov3)
submenu2.add_command(label="Кепка BlackHawk", command=gonna_tov3)
submenu3.add_command(label="Январь 2022 г.", command=jan)
submenu3.add_command(label="Февраль 2022 г.", command=feb)
submenu3.add_command(label="Март 2022 г.", command=march)
submenu3.add_command(label="Апрель 2022 г.", command=april)
submenu3.add_command(label="Май 2022 г.", command=may)
submenu3.add_command(label="Июнь 2022 г.", command=june)
submenu3.add_command(label="Июль 2022 г.", command=july)
submenu3.add_command(label="Август 2022 г.", command=august)
submenu3.add_command(label="Сентябрь 2022 г.", command=sept)
submenu3.add_command(label="Октябрь 2022 г.", command=oct)
submenu3.add_command(label="Ноябрь 2022 г.", command=novem)
submenu3.add_command(label="Декабрь 2022 г.", command=december)

file_menu2 = Menu()
menu.add_cascade(label="Справка", menu=file_menu2)
file_menu2.add_command(label="О программе", command=spr1)
file_menu2.add_command(label="Разработчики", command=spr2)
file_menu2.add_command(label="Версия 1.0")
file_menu3 = Menu()
menu.add_cascade(label="Тема", menu=file_menu3)
file_menu3.add_command(label="Светлая", command=white)
file_menu3.add_command(label="Темная", command=black)

poetry = "ДОБРО ПОЖАЛОВАТЬ \nНА СТРАНИЦУ АДМИНИСТРАТОРА \nWILDBERRIES"
label2 = Label(text=poetry, justify=CENTER, bg="white", fg="black", font='Arial 24')
label2.place(relx=.04, rely=.3)

window.mainloop()
