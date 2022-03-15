import tkinter as tk
import tkinter.messagebox as tkm
import csv



def reg():
    # global fio, adress, tel, iin, udo_number, giving_date, gived_by
    fio = fio_entry.get()
    adress = adress_entry.get()
    tel = tel_entry.get()
    iin = iin_entry.get()
    udo_number = udo_number_entry.get()
    giving_date = giving_date_entry.get()
    gived_by = gived_by_entry.get()
    with open('names.csv', 'r+', newline='') as csvfile:
        fieldnames = ['ФИО', 'Адрес', 'Мобильный телефон', 'ИИН', 'Номер удостоверения', 'Дата выдачи','Кем выдано']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        fio = fio_entry.get()
        adress = adress_entry.get()
        tel = tel_entry.get()
        iin = iin_entry.get()
        udo_number = udo_number_entry.get()
        giving_date = giving_date_entry.get()
        gived_by = gived_by_entry.get()
       #writer = csv.writer(f)
        fio = fio_entry.get()
        adress = adress_entry.get()
        tel = tel_entry.get()
        iin = iin_entry.get()
        udo_number = udo_number_entry.get()
        giving_date = giving_date_entry.get()
        gived_by = gived_by_entry.get()
        writer.writerow({'ФИО': fio, 'Адрес': adress, 'Мобильный телефон': tel, 'ИИН': iin, 'Номер удостоверения': udo_number,'Дата выдачи': giving_date, 'Кем выдано': gived_by})
    if tkm.askokcancel('Регистрация прошла успешно', 'Сейчас вы перейдете на новую страницу'):
        print('ВСЕ РАБОТАЕТ, ОКНО ЗАКРОЕТСЯ')
        window.destroy()



window = tk.Tk()
window.title('Регистрация')
window.geometry('600x600')
window.configure(bg='#7B68EE')

# main_menu = tk.Menu(window)
# window.configure(menu=main_menu)
# file_menu = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label='SOME', menu=file_menu)

author_label = tk.Label(window, text='Авторы: Вагина О., Серикова Д., Бурханов Р., Кушманов Е.', bg='#7B68EE' )
author_label.place(relx=0, rely=1, anchor='sw')

reg_label = tk.Label(window, text='Регистрация',
                     font=('Kharkiv', 20), bg='#7B68EE')
reg_label.place(x=175, y=75)

fio_label = tk.Label(window, text='Введите ФИО:', bg='#7B68EE')
fio_entry = tk.Entry(window)
fio_label.place(x=98, y=150)
fio_entry.place(x=250, y=150)

adress_label = tk.Label(window, text='Введите адрес:', bg='#7B68EE')
adress_entry = tk.Entry(window)
adress_label.place(x=98, y=200)
adress_entry.place(x=250, y=200)

tel_label = tk.Label(window, text='Введите телефон:', bg='#7B68EE')
tel_entry = tk.Entry(window)
tel_label.place(x=98, y=250)
tel_entry.place(x=250, y=250)

iin_label = tk.Label(window, text='Введите ИИН:', bg='#7B68EE')
iin_entry = tk.Entry(window)
iin_label.place(x=98, y=300)
iin_entry.place(x=250, y=300)

udo_number_label = tk.Label(window, text='Введите номер:', bg='#7B68EE')
udo_number_entry = tk.Entry(window)
udo_number_label.place(x=98, y=350)
udo_number_entry.place(x=250, y=350)

giving_date_label = tk.Label(window, text='Введите дату выдачи:', bg='#7B68EE')
giving_date_entry = tk.Entry(window)
giving_date_label.place(x=98, y=400)
giving_date_entry.place(x=250, y=400)

gived_by_label = tk.Label(window, text='Введите кем выдано:', bg='#7B68EE')
gived_by_entry = tk.Entry(window)
gived_by_label.place(x=98, y=450)
gived_by_entry.place(x=250, y=450)

reg_button = tk.Button(window, text='Зарегистрироваться', command=reg)
reg_button.place(x=225, y=525)


window.mainloop()
