
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import REG_support


def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(REG_support.root, tearoff=0)
        Popupmenu1.configure(activebackground="#7B68EE")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#7B68EE")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)


def popup2(event, *args, **kwargs):
        Popupmenu2 = tk.Menu(REG_support.root, tearoff=0)
        Popupmenu2.configure(activebackground="#ececec")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="#000000")
        Popupmenu2.configure(background="#7B68EE")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(foreground="#000000")
        Popupmenu2.post(event.x_root, event.y_root)

def popup3(event, *args, **kwargs):
        Popupmenu3 = tk.Menu(REG_support.root, tearoff=0)
        Popupmenu3.configure(activebackground="#ececec")
        Popupmenu3.configure(activeborderwidth="1")
        Popupmenu3.configure(activeforeground="#000000")
        Popupmenu3.configure(background="#7B68EE")
        Popupmenu3.configure(borderwidth="1")
        Popupmenu3.configure(disabledforeground="#a3a3a3")
        Popupmenu3.configure(foreground="#000000")
        Popupmenu3.post(event.x_root, event.y_root)

def popup4(event, *args, **kwargs):
        Popupmenu4 = tk.Menu(REG_support.root, tearoff=0)
        Popupmenu4.configure(activebackground="#ececec")
        Popupmenu4.configure(activeborderwidth="1")
        Popupmenu4.configure(activeforeground="#000000")
        Popupmenu4.configure(background="#7B68EE")
        Popupmenu4.configure(borderwidth="1")
        Popupmenu4.configure(disabledforeground="#a3a3a3")
        Popupmenu4.configure(foreground="#000000")
        Popupmenu4.post(event.x_root, event.y_root)

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#7B68EE'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#7B68EE' # X11 color: 'gray85'
        _ana1color = '#7B68EE' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x600+300+78")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("WILDBERRIES")
        top.configure(relief="groove")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#7B68EE")
        top.configure(highlightcolor="black")

        self.top = top
        self.che63 = tk.IntVar()
        self.che68 = tk.IntVar()

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=81, width=604)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#7B68EE")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Times New Roman} -size 20")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#7B68EE")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''WILDBERRIES''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.083, rely=0.3, height=61, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#7B68EE")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Times New Roman} -size 16")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#7B68EE")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief="raised")
        self.Label2.configure(text='''Логин''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.083, rely=0.45, height=61, width=144)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#7B68EE")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Times New Roman} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#7B68EE")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Пароль''')

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.417, rely=0.3, height=60, relwidth=0.523)
        self.Entry1.configure(background="#c0c0c0")
        self.Entry1.configure(borderwidth="2")
        self.Entry1.configure(cursor="")
        self.Entry1.configure(disabledforeground="#dcb4a5")
        self.Entry1.configure(font="-family {Times New Roman} -size 14")
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(highlightbackground="#7B68EE")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(readonlybackground="#ffffff")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="black")

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.267, rely=0.15, height=41, width=314)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#7B68EE")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Times New Roman} -size 20")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#7B68EE")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Вход в систему''')

        self.Checkbutton1 = tk.Checkbutton(self.top)
        self.Checkbutton1.place(relx=0.183, rely=0.6, relheight=0.058
                , relwidth=0.268)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#7B68EE")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#7B68EE")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Администратор''')
        self.Checkbutton1.configure(variable=self.che63)

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.383, rely=0.683, height=34, width=157)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#7B68EE")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Times New Roman} -size 14 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#7B68EE")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Войти''')

        self.Checkbutton2 = tk.Checkbutton(self.top)
        self.Checkbutton2.place(relx=0.583, rely=0.6, relheight=0.058
                , relwidth=0.268)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#7B68EE")
        self.Checkbutton2.configure(compound='left')
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#7B68EE")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Покупатель''')
        self.Checkbutton2.configure(variable=self.che68)

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.417, rely=0.45, height=60, relwidth=0.523)
        self.Entry1.configure(background="#c0c0c0")
        self.Entry1.configure(disabledforeground="#000000")
        self.Entry1.configure(font="-family {Times New Roman} -size 14")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#7B68EE")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="black")

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.383, rely=0.767, height=34, width=157)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#7B68EE")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Times New Roman} -size 14 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#7B68EE")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Регистрация''')

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.0, rely=0.867, height=81, width=604)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='s')
        self.Label1_1.configure(background="#7B68EE")
        self.Label1_1.configure(compound='right')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Times New Roman} -size 14")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#7B68EE")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Вагина О., Бурханов Р., Серикова Д., Кушманов Е.''')

def start_up():
    REG_support.main()

if __name__ == '__main__':
    REG_support.main()



