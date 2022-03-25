
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *



def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
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
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("730x624+500+154")
        top.minsize(120, 1)
        top.maxsize(1711, 1028)
        top.resizable(1,  1)
        top.title("Заказы")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                label="Каталог товаров")
        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="Товары и заказы")
        self.sub_menu.add_command(
                label="Корзина")
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Справка")
        self.sub_menu1.add_command(
                label="О программе")
        self.sub_menu1.add_command(
                label="Разработчики")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.329, rely=0.0, height=59, width=267)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 18")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Оформленные заказы''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.095, rely=0.127, height=24, width=107)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 13")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''№ заказа:''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.423, rely=0.127, height=24, width=38)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 13")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''1''')

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.095, rely=0.181, height=35, width=232)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(cursor="fleur")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 13")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Наименование товара:''')

        self.Label5 = tk.Label(self.top)
        self.Label5.place(relx=0.423, rely=0.181, height=35, width=153)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 13")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Кепка LAOCHRA''')

        self.Label6 = tk.Label(self.top)
        self.Label6.place(relx=0.095, rely=0.236, height=23, width=176)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(cursor="fleur")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 13")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Цена за единицу:''')

        self.Label7 = tk.Label(self.top)
        self.Label7.place(relx=0.423, rely=0.236, height=23, width=84)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 13")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''4999 тг.''')

        self.TSeparator1 = ttk.Separator(self.top)
        self.TSeparator1.place(relx=0.078, rely=0.181,  relwidth=0.784)

        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=0.078, rely=0.107,  relheight=0.308)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.078, rely=0.107,  relwidth=0.782)

        self.TSeparator4 = ttk.Separator(self.top)
        self.TSeparator4.place(relx=0.407, rely=0.107,  relheight=0.308)
        self.TSeparator4.configure(orient="vertical")

        self.TSeparator5 = ttk.Separator(self.top)
        self.TSeparator5.place(relx=0.86, rely=0.107,  relheight=0.306)
        self.TSeparator5.configure(orient="vertical")

        self.TSeparator6 = ttk.Separator(self.top)
        self.TSeparator6.place(relx=0.078, rely=0.417,  relwidth=0.782)

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.095, rely=0.271, height=44, width=143)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Segoe UI} -size 13")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Количество:''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(relx=0.095, rely=0.345, height=43, width=165)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="-family {Segoe UI} -size 13")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Стоимость:''')
        self.TLabel2.configure(compound='left')

        self.TSeparator7 = ttk.Separator(self.top)
        self.TSeparator7.place(relx=0.078, rely=0.345,  relwidth=0.782)
        self.TSeparator7.configure(cursor="fleur")

        self.TLabel3 = ttk.Label(self.top)
        self.TLabel3.place(relx=0.423, rely=0.271, height=44, width=51)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="-family {Segoe UI} -size 13")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''2''')
        self.TLabel3.configure(compound='left')

        self.TLabel4 = ttk.Label(self.top)
        self.TLabel4.place(relx=0.423, rely=0.345, height=44, width=121)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="-family {Segoe UI} -size 13")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''9998 тг.''')
        self.TLabel4.configure(compound='left')

        self.TSeparator8 = ttk.Separator(self.top)
        self.TSeparator8.place(relx=0.407, rely=0.345,  relwidth=0.314)

        self.TSeparator9 = ttk.Separator(self.top)
        self.TSeparator9.place(relx=0.082, rely=0.481,  relwidth=0.782)

        self.TSeparator10 = ttk.Separator(self.top)
        self.TSeparator10.place(relx=0.082, rely=0.545,  relwidth=0.782)

        self.TSeparator11 = ttk.Separator(self.top)
        self.TSeparator11.place(relx=0.082, rely=0.705,  relwidth=0.782)

        self.TSeparator12 = ttk.Separator(self.top)
        self.TSeparator12.place(relx=0.082, rely=0.785,  relwidth=0.782)

        self.TSeparator13 = ttk.Separator(self.top)
        self.TSeparator13.place(relx=0.082, rely=0.481,  relheight=0.308)
        self.TSeparator13.configure(orient="vertical")

        self.TSeparator14 = ttk.Separator(self.top)
        self.TSeparator14.place(relx=0.863, rely=0.481,  relheight=0.308)
        self.TSeparator14.configure(orient="vertical")

        self.TSeparator15 = ttk.Separator(self.top)
        self.TSeparator15.place(relx=0.411, rely=0.481,  relheight=0.308)
        self.TSeparator15.configure(orient="vertical")

        self.Label2_1 = tk.Label(self.top)
        self.Label2_1.place(relx=0.096, rely=0.497, height=24, width=107)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Segoe UI} -size 13")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''№ заказа:''')

        self.Label4_1 = tk.Label(self.top)
        self.Label4_1.place(relx=0.096, rely=0.545, height=35, width=233)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(activeforeground="black")
        self.Label4_1.configure(anchor='w')
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(compound='left')
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(font="-family {Segoe UI} -size 13")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''Наименование товара:''')

        self.Label6_1 = tk.Label(self.top)
        self.Label6_1.place(relx=0.096, rely=0.593, height=24, width=176)
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(activeforeground="black")
        self.Label6_1.configure(anchor='w')
        self.Label6_1.configure(background="#d9d9d9")
        self.Label6_1.configure(compound='left')
        self.Label6_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1.configure(font="-family {Segoe UI} -size 13")
        self.Label6_1.configure(foreground="#000000")
        self.Label6_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1.configure(highlightcolor="black")
        self.Label6_1.configure(text='''Цена за единицу:''')

        self.TLabel1_1 = ttk.Label(self.top)
        self.TLabel1_1.place(relx=0.096, rely=0.641, height=44, width=143)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="-family {Segoe UI} -size 13")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Количество:''')
        self.TLabel1_1.configure(compound='left')

        self.TLabel2_1 = ttk.Label(self.top)
        self.TLabel2_1.place(relx=0.096, rely=0.705, height=43, width=166)
        self.TLabel2_1.configure(background="#d9d9d9")
        self.TLabel2_1.configure(foreground="#000000")
        self.TLabel2_1.configure(font="-family {Segoe UI} -size 13")
        self.TLabel2_1.configure(relief="flat")
        self.TLabel2_1.configure(anchor='w')
        self.TLabel2_1.configure(justify='left')
        self.TLabel2_1.configure(text='''Стоимость:''')
        self.TLabel2_1.configure(compound='left')

        self.TSeparator16 = ttk.Separator(self.top)
        self.TSeparator16.place(relx=0.082, rely=0.705,  relwidth=0.312)

        self.TSeparator17 = ttk.Separator(self.top)
        self.TSeparator17.place(relx=0.096, rely=0.545,  relwidth=0.312)

        self.TSeparator18 = ttk.Separator(self.top)
        self.TSeparator18.place(relx=0.411, rely=0.497,  relheight=0.271)
        self.TSeparator18.configure(orient="vertical")

        self.Label5_1 = tk.Label(self.top)
        self.Label5_1.place(relx=0.425, rely=0.545, height=35, width=154)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(anchor='w')
        self.Label5_1.configure(background="#d9d9d9")
        self.Label5_1.configure(compound='left')
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(font="-family {Segoe UI} -size 13")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''Кепка BlackHawk''')

        self.Label7_1 = tk.Label(self.top)
        self.Label7_1.place(relx=0.425, rely=0.593, height=24, width=85)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="black")
        self.Label7_1.configure(anchor='w')
        self.Label7_1.configure(background="#d9d9d9")
        self.Label7_1.configure(compound='left')
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font="-family {Segoe UI} -size 13")
        self.Label7_1.configure(foreground="#000000")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''3999 тг.''')

        self.TLabel3_1 = ttk.Label(self.top)
        self.TLabel3_1.place(relx=0.425, rely=0.641, height=44, width=51)
        self.TLabel3_1.configure(background="#d9d9d9")
        self.TLabel3_1.configure(foreground="#000000")
        self.TLabel3_1.configure(font="-family {Segoe UI} -size 13")
        self.TLabel3_1.configure(relief="flat")
        self.TLabel3_1.configure(anchor='w')
        self.TLabel3_1.configure(justify='left')
        self.TLabel3_1.configure(text='''1''')
        self.TLabel3_1.configure(compound='left')

        self.TSeparator19 = ttk.Separator(self.top)
        self.TSeparator19.place(relx=0.411, rely=0.545,  relwidth=0.312)

        self.TLabel4_1 = ttk.Label(self.top)
        self.TLabel4_1.place(relx=0.425, rely=0.705, height=44, width=121)
        self.TLabel4_1.configure(background="#d9d9d9")
        self.TLabel4_1.configure(foreground="#000000")
        self.TLabel4_1.configure(font="-family {Segoe UI} -size 13")
        self.TLabel4_1.configure(relief="flat")
        self.TLabel4_1.configure(anchor='w')
        self.TLabel4_1.configure(justify='left')
        self.TLabel4_1.configure(text='''3999 тг.''')
        self.TLabel4_1.configure(compound='left')

        self.TSeparator20 = ttk.Separator(self.top)
        self.TSeparator20.place(relx=0.342, rely=0.705,  relwidth=0.311)

        self.TLabel5 = ttk.Label(self.top)
        self.TLabel5.place(relx=0.082, rely=0.817, height=32, width=166)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="-family {Segoe UI} -size 13")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Итоговая сумма:''')
        self.TLabel5.configure(compound='left')

        self.TLabel6 = ttk.Label(self.top)
        self.TLabel6.place(relx=0.288, rely=0.817, height=32, width=97)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="-family {Segoe UI} -size 13")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''13997 тг.''')
        self.TLabel6.configure(compound='left')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.329, rely=0.897, height=24, width=227)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''ОСТАВИТЬ ОТЗЫВ О ПРИЛОЖЕНИИ''')

        self.TLabel3_2 = ttk.Label(self.top)
        self.TLabel3_2.place(relx=0.438, rely=0.481, height=44, width=51)
        self.TLabel3_2.configure(background="#d9d9d9")
        self.TLabel3_2.configure(foreground="#000000")
        self.TLabel3_2.configure(font="-family {Segoe UI} -size 13")
        self.TLabel3_2.configure(relief="flat")
        self.TLabel3_2.configure(anchor='w')
        self.TLabel3_2.configure(justify='left')
        self.TLabel3_2.configure(text='''2''')
        self.TLabel3_2.configure(compound='left')

        self.TSeparator21 = ttk.Separator(self.top)
        self.TSeparator21.place(relx=0.425, rely=0.545,  relwidth=0.312)

        self.TSeparator22 = ttk.Separator(self.top)
        self.TSeparator22.place(relx=0.342, rely=0.481,  relwidth=0.274)



if __name__ == '__main__':
    main()




