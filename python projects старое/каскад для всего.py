from cgitb import text
import tkinter as tk

window = tk.Tk()
window.title('Main Page')
window.geometry('600x600')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='SOME', menu=file_menu)

author_label = tk.Label(window, text='Serikova')
author_label.place(relx=0, rely=1, anchor='sw')




window.mainloop()
