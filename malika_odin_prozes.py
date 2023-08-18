from tkinter import *
from tkinter import ttk
import tkinter as tk
import time, sys, datetime
from threading import Thread
from time import sleep

sl = {}#словарь - ведомость за день 
##skan = '0'#переменная для ввода номера плазмы или лотка
sp = []#список номеров плазм
spt = []#список времен укладки и забора плазмы  
ff_lotok = []#номер лотка
##n = 0
m = 0

def click_button1():
    name_entry['state'] = "disabled"
    print('процес')


def check(*args):
    ##str_t = ''
    ##global n
    global m
    global ff_lotok
    global time_string
    global time_string1   
    ff = name.get()

    if  m == 0 and len(ff) == 10 and int(ff[0]) == 4:
        sp.append(ff)
        print('введите значения повторно')
        print('len(sp)',len(sp) )
        n = int(len(sp)) 
        print('sp=',sp)
        result.set(f'Отсканировано {n} пакетов плазмы.')
        name_entry.delete(0, last= END)

    if m == 1 and ff_lotok == ff:
        print('процес закончился')
        named_tuple = time.localtime() # получить struct_time
        time_string1 = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        #spt.append(time_string)
        for i in sp:
            sl[i] = spt
            str_o = i + ' / ' + time_string + ' / ' + time_string1 + '\n'
            file = open('E:\\fleshka\\malika\\1.txt','a')
            file.write(str_o)
        name_entry.delete(0, last= END)
        result.set(f'Процес закончился')
        click_button1()
        sys.exit(0) 

    if m == 0 and len(ff) == 16:
        ff_lotok = ff
        ##print('процес начался') 
        named_tuple = time.localtime() # получем кортеж из дат и времени
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)# получем дату и время укладки плазмы
        m = m + 1
        spt.append(time_string)
        name_entry.delete(0, last= END)
        name_entry['state'] = "disabled"
        result.set(f'Уложите плазму в шокерную')
        time.sleep(10)
        name_entry['state'] = "NORMA"
        result.set(f'Достанте плазму')

def click_button():
    name_entry['state'] = "NORMA"


root = tk.Tk()#создаем корневой объект - окно    
root.title("Приложення обліку шокувань")     # устанавливаем заголовок окна
root.geometry("700x950+100+10")# устанавливаем размеры и расположение окна
root.resizable(False, False) # запрещаем изменять окно 

# создаем основную текстовую метку
lbosn = tk.Label(root, text = "Здраствуй Маліка!",
               font = ('Arial', 16, 'bold'), width = 18, height = 2, relief = tk.RAISED, bd = 1)
                                        # создаем текстовую метку, определяем где размещаем и текст,
                                        #width - ширина, height - высота в знаках, relief = граница
                                        #bd - ширина границ
lbosn.grid(row=0, column=0, columnspan = 2, stick = 'we')    # размещаем метку в окне

#создаем 1 текстовую метку
lb1 = tk.Label(root, text = '''Отсканируйте
плазму!''', relief = tk.RAISED, bd = 1,
               width = 18, height = 3) # создаем текстовую метку, тройные ковычки
                                        # и перенос текста на новую строку - создание
                                        #многострочного текста 
lb1.grid(row=1, column=0, stick = 'ns')    # размещаем метку в окне

# создаем окно Entry
name = StringVar()
name_entry = ttk.Entry(textvariable=name, state = DISABLED) # окно исходно не активно
name_entry.grid(row=1, column=1, ipadx = 5, ipady = 32)    # размещаем метку Entry в окне
name_entry.focus_set() 

# создаем 2 текстовую метку
result = StringVar()
lb2 = ttk.Label(textvariable=result, borderwidth=2,
                            relief="ridge", padding=8, width = 18)
lb2.grid(row=1, column=2, stick = 'ns')

# создаем кнопку
btn1 = tk.Button(root, text = 'Почінаем шокування!', width = 18, height = 5, command=click_button) 
btn1.grid(row=1, column=3, stick = 'w')    # размещаем метку в окне

# отслеживаем изменение значения переменной name
name.trace_add("write", check)#запускаем функцию check при изменении 

root.mainloop()#запускает цикл обработки событий;
                #пока мы не вызовем эту функцию, наше окно
                #не будет реагировать на внешние раздражители.
