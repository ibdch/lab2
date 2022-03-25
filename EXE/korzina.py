
import pathlib
from pygubu.widgets.scrolledframe import ScrolledFrame
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


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


def opening1():
    root.destroy()

    PROJECT_PATH = pathlib.Path(__file__).parent
    PROJECT_UI = PROJECT_PATH / "AKSSSSANIII.ui"

    class AkssssaniiiApp:
        def __init__(self, master=None):
            # build ui
            self.toplevel2 = tk.Toplevel(master, container='false')
            self.scrolledframe17 = ScrolledFrame(self.toplevel2, scrolltype='both')
            self.label23 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_7 = tk.PhotoImage(file='7.png')
            self.label23.configure(image=self.img_7, text='label23')
            self.label23.place(anchor='nw', relx='0.04', rely='0.05', x='0', y='0')
            self.label24 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_1 = tk.PhotoImage(file='1.png')
            self.label24.configure(image=self.img_1, text='label24')
            self.label24.place(anchor='nw', relx='0.39', rely='0.05', x='0', y='0')
            self.label25 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_5 = tk.PhotoImage(file='5.png')
            self.label25.configure(image=self.img_5, text='label25')
            self.label25.place(anchor='nw', relx='0.73', rely='0.05', x='0', y='0')
            self.label26 = ttk.Label(self.scrolledframe17.innerframe)
            self.label26.configure(anchor='center', font='{Segoe UI} 13 {}', justify='center', relief='flat')
            self.label26.configure(takefocus=False, text='Кепка PUMA')
            self.label26.place(anchor='nw', bordermode='inside', height='20', relx='0.09', rely='0.02')
            self.label27 = ttk.Label(self.scrolledframe17.innerframe)
            self.label27.configure(font='{Segoe UI} 13 {}', text='Кепка NIKE')
            self.label27.place(anchor='nw', height='20', relx='0.445', rely='0.02', x='0', y='0')
            self.label28 = ttk.Label(self.scrolledframe17.innerframe)
            self.label28.configure(font='{Segoe UI} 13 {}', text='Кепка NORTH FACE')
            self.label28.place(anchor='nw', height='20', relx='0.75', rely='0.02', x='0', y='0')
            self.button1 = ttk.Button(self.scrolledframe17.innerframe)
            self.button1.configure(text='Добавить в корзину')
            self.button1.place(anchor='nw', relx='0.075', rely='0.27', x='0', y='0')
            self.label1 = ttk.Label(self.scrolledframe17.innerframe)
            self.label1.configure(takefocus=False)
            self.label1.grid(column='0', row='0')
            self.label2 = ttk.Label(self.scrolledframe17.innerframe)
            self.label2.grid(column='0', row='1')
            self.label3 = ttk.Label(self.scrolledframe17.innerframe)
            self.label3.grid(column='0', row='2')
            self.label4 = ttk.Label(self.scrolledframe17.innerframe)
            self.label4.grid(column='0', row='3')
            self.label5 = ttk.Label(self.scrolledframe17.innerframe)
            self.label5.grid(column='0', row='4')
            self.label6 = ttk.Label(self.scrolledframe17.innerframe)
            self.label6.grid(column='0', row='5')
            self.label7 = ttk.Label(self.scrolledframe17.innerframe)
            self.label7.grid(column='0', row='6')
            self.label8 = ttk.Label(self.scrolledframe17.innerframe)
            self.label8.configure(text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            self.label8.grid(column='0', row='7')
            self.label9 = ttk.Label(self.scrolledframe17.innerframe)
            self.label9.grid(column='0', row='8')
            self.label10 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_6 = tk.PhotoImage(file='6.png')
            self.label10.configure(image=self.img_6, text='label10')
            self.label10.place(anchor='nw', relx='0.04', rely='0.35', x='0', y='0')
            self.label11 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_41 = tk.PhotoImage(file='4 (1).png')
            self.label11.configure(image=self.img_41, text='label11')
            self.label11.place(anchor='nw', relx='0.39', rely='0.35', x='0', y='0')
            self.label12 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_2 = tk.PhotoImage(file='2.png')
            self.label12.configure(image=self.img_2, text='label12')
            self.label12.place(anchor='nw', relx='0.73', rely='0.35', x='0', y='0')
            self.label13 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_8 = tk.PhotoImage(file='8.png')
            self.label13.configure(image=self.img_8, text='label13')
            self.label13.place(anchor='nw', relx='0.04', rely='0.65', x='0', y='0')
            self.label14 = ttk.Label(self.scrolledframe17.innerframe)
            self.label14.grid(column='0', row='13')
            self.label15 = ttk.Label(self.scrolledframe17.innerframe)
            self.label15.configure(font='{Segoe UI} 13 {}', text='Кепка RAVENA')
            self.label15.place(anchor='nw', relx='0.084', rely='0.32', x='0', y='0')
            self.label16 = ttk.Label(self.scrolledframe17.innerframe)
            self.label16.configure(font='{Segoe UI} 13 {}', text='Кепка AKSSSANI')
            self.label16.place(anchor='nw', relx='0.42', rely='0.32', x='0', y='0')
            self.label17 = ttk.Label(self.scrolledframe17.innerframe)
            self.label17.configure(font='{Segoe UI} 13 {}', text='Кепка LAOCHRA')
            self.label17.place(anchor='nw', relx='0.76', rely='0.32', x='0', y='0')
            self.label21 = ttk.Label(self.scrolledframe17.innerframe)
            self.label21.configure(text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            self.label21.grid(column='0', row='20')
            self.button2 = ttk.Button(self.scrolledframe17.innerframe)
            self.button2.configure(text='Добавить в корзину')
            self.button2.place(anchor='nw', relx='0.43', rely='0.27', x='0', y='0')
            self.button3 = ttk.Button(self.scrolledframe17.innerframe)
            self.button3.configure(text='Добавить в корзину')
            self.button3.place(anchor='nw', relx='0.77', rely='0.27', x='0', y='0')
            self.button4 = ttk.Button(self.scrolledframe17.innerframe)
            self.button4.configure(text='Добавить в корзину')
            self.button4.place(anchor='nw', relx='0.43', rely='0.57', x='0', y='0')
            self.button5 = ttk.Button(self.scrolledframe17.innerframe)
            self.button5.configure(text='Добавить в корзину')
            self.button5.place(anchor='nw', relx='0.075', rely='0.57', x='0', y='0')
            self.button6 = ttk.Button(self.scrolledframe17.innerframe)
            self.button6.configure(text='Добавить в корзину')
            self.button6.place(anchor='nw', relx='0.77', rely='0.57', x='0', y='0')
            self.label51 = ttk.Label(self.scrolledframe17.innerframe)
            self.label51.configure(font='{Segoe UI} 13 {}', text='Кепка BlackHawk')
            self.label51.place(anchor='nw', relx='0.07', rely='0.62', x='0', y='0')
            self.button7 = ttk.Button(self.scrolledframe17.innerframe)
            self.button7.configure(text='Добавить в корзину')
            self.button7.place(anchor='nw', relx='0.075', rely='0.87', x='0', y='0')
            self.label52 = ttk.Label(self.scrolledframe17.innerframe)
            self.label52.configure(font='{Segoe UI} 13 {}', text='Кепка KINZA')
            self.label52.place(anchor='nw', relx='0.45', rely='0.62', x='0', y='0')
            self.label53 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_9 = tk.PhotoImage(file='9.png')
            self.label53.configure(image=self.img_9, justify='right', text='label53')
            self.label53.place(anchor='nw', relx='0.39', rely='0.65', x='0', y='0')
            self.label54 = ttk.Label(self.scrolledframe17.innerframe)
            self.img_3 = tk.PhotoImage(file='3.png')
            self.label54.configure(image=self.img_3, text='label54')
            self.label54.place(anchor='nw', relx='0.73', rely='0.65', x='0', y='0')
            self.label55 = ttk.Label(self.scrolledframe17.innerframe)
            self.label55.configure(font='{Segoe UI} 13 {}', text='Кепка KAMARR')
            self.label55.place(anchor='nw', relx='0.76', rely='0.62', x='0', y='0')
            self.button8 = ttk.Button(self.scrolledframe17.innerframe)
            self.button8.configure(text='Добавить в корзину')
            self.button8.place(anchor='nw', relx='0.43', rely='0.87', x='0', y='0')
            self.button9 = ttk.Button(self.scrolledframe17.innerframe)
            self.button9.configure(text='Добавить в корзину')
            self.button9.place(anchor='nw', relx='0.77', rely='0.87', x='0', y='0')
            self.label57 = ttk.Label(self.scrolledframe17.innerframe)
            self.label57.configure(font='{Segoe UI} 12 {}', text='4999 тг.')
            self.label57.place(anchor='nw', relx='0.12', rely='0.24', x='0', y='0')
            self.label58 = ttk.Label(self.scrolledframe17.innerframe)
            self.label58.configure(font='{Segoe UI} 12 {}', text='4499 тг.')
            self.label58.place(anchor='nw', relx='0.47', rely='0.24', x='0', y='0')
            self.label59 = ttk.Label(self.scrolledframe17.innerframe)
            self.label59.configure(font='{Segoe UI} 12 {}', text='5499 тг.')
            self.label59.place(anchor='nw', relx='0.81', rely='0.24', x='0', y='0')
            self.label62 = ttk.Label(self.scrolledframe17.innerframe)
            self.label62.configure(font='{Segoe UI} 12 {}', text='3499 тг.')
            self.label62.place(anchor='nw', relx='0.12', rely='0.54', x='0', y='0')
            self.label63 = ttk.Label(self.scrolledframe17.innerframe)
            self.label63.configure(font='{Segoe UI} 12 {}', text='4999 тг.')
            self.label63.place(anchor='nw', relx='0.12', rely='0.84', x='0', y='0')
            self.label64 = ttk.Label(self.scrolledframe17.innerframe)
            self.label64.configure(font='{Segoe UI} 12 {}', text='4499 тг.')
            self.label64.place(anchor='nw', relx='0.47', rely='0.54', x='0', y='0')
            self.label65 = ttk.Label(self.scrolledframe17.innerframe)
            self.label65.configure(font='{Segoe UI} 12 {}', text='4999 тг.')
            self.label65.place(anchor='nw', relx='0.81', rely='0.54', x='0', y='0')
            self.label66 = ttk.Label(self.scrolledframe17.innerframe)
            self.label66.configure(font='{Segoe UI} 12 {}', text='5999 тг.')
            self.label66.place(anchor='nw', relx='0.47', rely='0.84', x='0', y='0')
            self.label67 = ttk.Label(self.scrolledframe17.innerframe)
            self.label67.configure(font='{Segoe UI} 12 {}', text='3999 тг.')
            self.label67.place(anchor='nw', relx='0.81', rely='0.84', x='0', y='0')
            self.button10 = ttk.Button(self.scrolledframe17.innerframe)
            self.button10.configure(text='ПЕРЕЙТИ К КОРЗИНЕ')
            self.button10.place(anchor='nw', relx='0.42', rely='0.93', x='0', y='0')
            self.scrolledframe17.configure(usemousewheel=False)
            self.scrolledframe17.place(anchor='nw', height='461', relheight='0.0', relwidth='0.0', relx='0.0',
                                       rely='0.28',
                                       width='800', x='0', y='0')
            self.label60 = ttk.Label(self.toplevel2)
            self.label60.configure(background='#f0f0f0', font='{Segoe UI Emoji} 18 {}', text='КАТАЛОГ ТОВАРОВ')
            self.label60.place(anchor='nw', relx='0.38', rely='0.19', x='0', y='0')
            self.label61 = ttk.Label(self.toplevel2)
            self.img_imgonlinecomuaResizeQzO7HQKLLg8UE4 = tk.PhotoImage(
                file='imgonline-com-ua-Resize-QzO7HQKLLg8UE4.png')
            self.label61.configure(image=self.img_imgonlinecomuaResizeQzO7HQKLLg8UE4, text='label61')
            self.label61.place(anchor='nw', relx='0.24', rely='0.06', x='0', y='0')
            self.toplevel2.configure(background='#f0f0f0', cursor='arrow', height='200', relief='flat')
            self.toplevel2.configure(width='200')
            self.toplevel2.geometry('800x641')
            self.toplevel2.resizable(True, True)

            # Main widget
            self.mainwindow = self.toplevel2

        def run(self):
            self.mainwindow.mainloop()

    if __name__ == '__main__':
        app = AkssssaniiiApp()
        app.run()


def opening2():
    root.destroy()
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


    def kai():
        root.destroy()
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

        def exit1():
            root.destroy()


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

                top.geometry("517x183+553+205")
                top.minsize(120, 1)
                top.maxsize(1711, 1048)
                top.resizable(1, 1)
                top.title("Отзыв")
                top.configure(background="#d9d9d9")

                self.top = top

                self.Label1 = tk.Label(self.top)
                self.Label1.place(relx=0.193, rely=0.109, height=17, width=359)
                self.Label1.configure(anchor='w')
                self.Label1.configure(background="#d9d9d9")
                self.Label1.configure(compound='left')
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Segoe UI} -size 13")
                self.Label1.configure(foreground="#000000")
                self.Label1.configure(text='''Хотите оставить отзыв о приложении?''')

                self.TEntry1 = ttk.Entry(self.top)
                self.TEntry1.place(relx=0.077, rely=0.273, relheight=0.224
                                   , relwidth=0.863)
                self.TEntry1.configure(validate="focus")
                self.TEntry1.configure(takefocus="")
                self.TEntry1.configure(cursor="fleur")
                self.tooltip_font = "TkDefaultFont"
                self.TEntry1_tooltip = \
                    ToolTip(self.TEntry1, self.tooltip_font, '''Ваш отзыв''')

                self.Label2 = tk.Label(self.top)
                self.Label2.place(relx=0.232, rely=0.765, height=26, width=284)
                self.Label2.configure(anchor='w')
                self.Label2.configure(background="#d9d9d9")
                self.Label2.configure(compound='left')
                self.Label2.configure(cursor="fleur")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Segoe UI} -size 13")
                self.Label2.configure(foreground="#000000")
                self.Label2.configure(text='''Спасибо, мы учтем Ваше мнение!''')

                self.Button1 = tk.Button(self.top)
                self.Button1.place(relx=0.36, rely=0.57, height=24, width=140)
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
                self.Button1.configure(text='ОСТАВИТЬ ОТЗЫВ', command=exit1)

        # Support code for Balloon Help (also called tooltips).
        # derived from http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
        from time import time, localtime, strftime
        class ToolTip(tk.Toplevel):
            """ Provides a ToolTip widget for Tkinter. """

            def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                         delay=0.5, follow=True):
                self.wdgt = wdgt
                self.parent = self.wdgt.master
                tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
                self.withdraw()
                self.overrideredirect(True)
                self.msgVar = tk.StringVar()
                if msg is None:
                    self.msgVar.set('No message provided')
                else:
                    self.msgVar.set(msg)
                self.msgFunc = msgFunc
                self.delay = delay
                self.follow = follow
                self.visible = 0
                self.lastMotion = 0
                tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                           font=tooltip_font,
                           aspect=1000).grid()
                self.wdgt.bind('<Enter>', self.spawn, '+')
                self.wdgt.bind('<Leave>', self.hide, '+')
                self.wdgt.bind('<Motion>', self.move, '+')

            def spawn(self, event=None):
                self.visible = 1
                self.after(int(self.delay * 1000), self.show)

            def show(self):
                if self.visible == 1 and time() - self.lastMotion > self.delay:
                    self.visible = 2
                if self.visible == 2:
                    self.deiconify()

            def move(self, event):
                self.lastMotion = time()
                if self.follow is False:
                    self.withdraw()
                    self.visible = 1
                self.geometry('+%i+%i' % (event.x_root + 20, event.y_root - 10))
                try:
                    self.msgVar.set(self.msgFunc())
                except:
                    pass
                self.after(int(self.delay * 1000), self.show)

            def hide(self, event=None):
                self.visible = 0
                self.withdraw()

            def update(self, msg):
                self.msgVar.set(msg)

        #                   End of Class ToolTip

        if __name__ == '__main__':
            main()

    def main5():
        root.destroy()
        import mainmy

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

            top.geometry("730x624+500+154")
            top.minsize(120, 1)
            top.maxsize(1711, 1028)
            top.resizable(1, 1)
            top.title("Заказы")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.top = top

            self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
            top.configure(menu=self.menubar)

            self.menubar.add_command(
                label="Каталог товаров", command=opening1)
            self.sub_menu = tk.Menu(top,
                                    activebackground="#ececec",
                                    activeborderwidth=1,
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    borderwidth=1,
                                    disabledforeground="#a3a3a3",
                                    foreground="#000000",
                                    tearoff=0)
            self.menubar.add_command(label="Перейти на главную страницу", command=main5)
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
            self.sub_menu1.add_command(label="О программе", command=opening3)
            self.sub_menu1.add_command(
                label="Разработчики", command=opening4)

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
            self.TSeparator1.place(relx=0.078, rely=0.181, relwidth=0.784)

            self.TSeparator2 = ttk.Separator(self.top)
            self.TSeparator2.place(relx=0.078, rely=0.107, relheight=0.308)
            self.TSeparator2.configure(orient="vertical")

            self.TSeparator3 = ttk.Separator(self.top)
            self.TSeparator3.place(relx=0.078, rely=0.107, relwidth=0.782)

            self.TSeparator4 = ttk.Separator(self.top)
            self.TSeparator4.place(relx=0.407, rely=0.107, relheight=0.308)
            self.TSeparator4.configure(orient="vertical")

            self.TSeparator5 = ttk.Separator(self.top)
            self.TSeparator5.place(relx=0.86, rely=0.107, relheight=0.306)
            self.TSeparator5.configure(orient="vertical")

            self.TSeparator6 = ttk.Separator(self.top)
            self.TSeparator6.place(relx=0.078, rely=0.417, relwidth=0.782)

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
            self.TSeparator7.place(relx=0.078, rely=0.345, relwidth=0.782)
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
            self.TSeparator8.place(relx=0.407, rely=0.345, relwidth=0.314)

            self.TSeparator9 = ttk.Separator(self.top)
            self.TSeparator9.place(relx=0.082, rely=0.481, relwidth=0.782)

            self.TSeparator10 = ttk.Separator(self.top)
            self.TSeparator10.place(relx=0.082, rely=0.545, relwidth=0.782)

            self.TSeparator11 = ttk.Separator(self.top)
            self.TSeparator11.place(relx=0.082, rely=0.705, relwidth=0.782)

            self.TSeparator12 = ttk.Separator(self.top)
            self.TSeparator12.place(relx=0.082, rely=0.785, relwidth=0.782)

            self.TSeparator13 = ttk.Separator(self.top)
            self.TSeparator13.place(relx=0.082, rely=0.481, relheight=0.308)
            self.TSeparator13.configure(orient="vertical")

            self.TSeparator14 = ttk.Separator(self.top)
            self.TSeparator14.place(relx=0.863, rely=0.481, relheight=0.308)
            self.TSeparator14.configure(orient="vertical")

            self.TSeparator15 = ttk.Separator(self.top)
            self.TSeparator15.place(relx=0.411, rely=0.481, relheight=0.308)
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
            self.TSeparator16.place(relx=0.082, rely=0.705, relwidth=0.312)

            self.TSeparator17 = ttk.Separator(self.top)
            self.TSeparator17.place(relx=0.096, rely=0.545, relwidth=0.312)

            self.TSeparator18 = ttk.Separator(self.top)
            self.TSeparator18.place(relx=0.411, rely=0.497, relheight=0.271)
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
            self.TSeparator19.place(relx=0.411, rely=0.545, relwidth=0.312)

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
            self.TSeparator20.place(relx=0.342, rely=0.705, relwidth=0.311)

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
            self.Button1.configure(text='''ОСТАВИТЬ ОТЗЫВ О ПРИЛОЖЕНИИ''', command=kai)

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
            self.TSeparator21.place(relx=0.425, rely=0.545, relwidth=0.312)

            self.TSeparator22 = ttk.Separator(self.top)
            self.TSeparator22.place(relx=0.342, rely=0.481, relwidth=0.274)

    if __name__ == '__main__':
        main()


def opening3():
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


def opening4():
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


def delete1():
    root.mainloop()
    import korzina1


def delete2():
    root.mainloop()
    import korzina2


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

        top.geometry("730x624+553+134")
        top.minsize(120, 1)
        top.maxsize(1711, 1028)
        top.resizable(1,  1)
        top.title("Корзина")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                label="Каталог товаров", command=opening1)
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
                label="Мои заказы", command=opening2)
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
                label="О программе", command=opening3)
        self.sub_menu1.add_command(
                label="Разработчики", command=opening4)

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
        self.Label1.configure(text='''Товары в корзине''')

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
        self.Button1.place(relx=0.397, rely=0.897, height=24, width=127)
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
        self.Button1.configure(text='''ОФОРМИТЬ ЗАКАЗ''', command=opening2)

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

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.89, rely=0.369, height=24, width=57)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Удалить''', command=delete1)

        self.Button2_1 = tk.Button(self.top)
        self.Button2_1.place(relx=0.89, rely=0.721, height=24, width=57)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#d9d9d9")
        self.Button2_1.configure(compound='left')
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text='''Удалить''', command=delete2)


if __name__ == '__main__':
    main()




