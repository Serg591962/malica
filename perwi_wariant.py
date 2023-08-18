from tkinter import *
import tkinter as tk
from tkinter import ttk
import time, sys
import datetime
from threading import Thread
from time import sleep
sl = {}#словарь - ведомость за день 
skan = '0'#переменная для ввода номера плазмы или лотка
sp = []#список номеров плазм
spt = []#список времен укладки и забора плазмы  
n = 0
m = 0
time_string = ''
time_string1 = ''
ff_lotok = 'a'

def add_labe1():
    lb1 = tk.Label(root, text = '''В окно справа ведите
или отсканируйте
номер плазмы!''', relief = tk.RAISED, bd = 1,
               width = 18, height = 2) # создаем текстовую метку, тройные ковычки
                                        # и перенос текста на новую строку - создание
                                        #многострочного текста 
    lb1.grid(row=1, column=1, stick = 'ns')    # размещаем метку в окне
    #def name_entry_delete():#ф очистки окна
        #name_entry.delete(0, last= END)


    def check(*args):
        str_t = ''
        global n
        global m
        global ff_lotok
        global time_string
        global time_string1   
        ff = name.get()
        if  ff_lotok == ff and m == 1:
            print('процес закончился')
            named_tuple = time.localtime() # получить struct_time
            time_string1 = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            #spt.append(time_string)
            for i in sp:
                sl[i] = spt
                str_o = i + ' / ' + time_string + ' / ' + time_string1 + '\n'
                file = open('E:\\fleshka\\tkinter\\1.txt','a')
                file.write(str_o)
            name_entry.delete(0, last= END)
            sys.exit(0)

        if int(ff[0]) == 4 and len(ff) == 10  and m == 0:
            ff_lotok = ff
            print('процес начался') 
            named_tuple = time.localtime() # получить struct_time
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            #spt.append(time_string)
            name_entry.delete(0, last= END)
            result = f'Уложите плазму в шокерную'
            time.sleep(10)
            ff_lotok = ff
            print('введите значения ключа повторно')
            result = f'Достанте плазму'

        if len(ff) == 16 and m == 0:
            sp.append(ff)
            print('введите значения повторно')
            print('len(sp)',len(sp) )
            n = int(len(sp)) 
            print('n=',n)
            textvariable.ser(f'Отсканировано {n} пакетов плазмы.')
            name_entry.delete(0, last= END)

    
    name = StringVar()
    name_entry = ttk.Entry(textvariable=name) 
    name_entry.grid(row=1, column=2, ipadx = 5, ipady = 20)    # размещаем метку Entry в окне
    name_entry.focus_set() 
    # отслеживаем изменение значения переменной name
    name.trace_add("write", check)#запускаем функцию check при изменении 

    result = StringVar()
    check_labe2 = ttk.Label(textvariable=result, borderwidth=2,
                            relief="ridge", padding=8, width = 18)
    check_labe2.grid(row=1, column=3, stick = 'ns')


    #btn2 = tk.Button(root, text = 'Ввод', width = 8, height = 3,
        #command = name_entry_delete) #запускаем очистку окна
    #btn2.grid(row=1, column=4, stick = 'w')    # размещаем метку Button в окне

#создаем корневой объект - окно 
root = tk.Tk()#создаем корневой объект - окно    
root.title("Приложення обліку шокувань")     # устанавливаем заголовок окна
root.geometry("700x950+100+10")# устанавливаем размеры и расположение окна
root.resizable(False, False) # запрещаем изменять окно 

# создаем текстовую метку
lbosn = tk.Label(root, text = "Здраствуй Маліка!",
               font = ('Arial', 16, 'bold'), width = 20, height = 2, relief = tk.RAISED, bd = 1)
                                        # создаем текстовую метку, определяем где размещаем и текст,
                                        #width - ширина, height - высота в знаках, relief = граница
                                        #bd - ширина границ
lbosn.grid(row=0, column=0, columnspan = 2, stick = 'we')    # размещаем метку в окне

# создаем 1 кнопку
btn1 = tk.Button(root, text = 'Почінаем шокування!', width = 18, height = 3,
                 command = add_labe1) #state = tk.DISABLED - кнопка выключена
btn1.grid(row=1, column=0, stick = 'w')    # размещаем метку в окне



root.mainloop()#запускает цикл обработки событий;
                #пока мы не вызовем эту функцию, наше окно
                #не будет реагировать на внешние раздражители.

