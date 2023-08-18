from tkinter import *
from tkinter import ttk
sp = []
        self.root = Tk()#создаем корневой объект - окно    
        self.root.title("Приложення обліку шокувань")     # устанавливаем заголовок окна
        self.root.geometry("700x950+100+10")# устанавливаем размеры и расположение окна
        self.root.resizable(False, False) # запрещаем изменять окно 
        self.row_ekz = row_ekz




class Test():
    def __init__(self,row_ekz ):


        # создаем окно Entry
        self.name = StringVar()
        self.result = StringVar()

        self.name_entry = ttk.Entry(textvariable=self.name) 
        self.name_entry.grid(row = row_ekz, column=1, ipadx = 5, ipady = 20)    # размещаем метку Entry в окне
        self.name_entry.focus_set() 


        # создаем 2 текстовую метку

        self.lb2 = ttk.Label(textvariable=self.result, borderwidth=2,
                            relief="ridge", padding=8, width = 18)
        self.lb2.grid(row = row_ekz, column=2, stick = 'ns')

        # отслеживаем изменение значения переменной name
        self.name.trace_add("write", self.check)#запускаем функцию check при изменении 


        self.root.mainloop()#запускает цикл обработки событий;
                #пока мы не вызовем эту функцию, наше окно
                #не будет реагировать на внешние раздражители.

    def check(*args):  
        ff = name.get()
        if len(ff) == 16:
            sp.append(ff)
            print('введите значения повторно')
            print('len(sp)',len(sp) )
            n = int(len(sp)) 
            print('n=',n)
            result.set(f'Отсканировано {n} пакетов плазмы.')
            name_entry.delete(0, last= END)    

app1=Test(1)
app2=Test(2)
