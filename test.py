import tkinter as tk 
from tkinter import *


window = tk.Tk()


label = tk.Label(window, text='Введите вашу сумму денег')
label.pack()




entery = tk.Entry()
entery.pack()




def change_lablel_text():
    rub = float(entery.get())
    dollar = tk.Label(window, text= "доллары -" + str(round(rub / 97, 2)) + f" при {rub} рублях")
    dollar.pack()

    euro = tk.Label(window, text= "евро -" + str(round(rub / 104.72, 2)) + f" при {rub} рублях") 
    euro.pack()

    yuan = tk.Label(window, text= "юани -" + str(round(rub / 13.31, 2)) + f" при {rub} рублях")
    yuan.pack()





butt = tk.Button(window, text="ок", command=change_lablel_text)
butt.pack()





window.mainloop()