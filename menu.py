#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
#from tkinter import Menu

"""
alphabet=list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
word=[]
indexes_of_keyword=[]         
indexes_of_word=[]            
encrypt_word=[]
indexes_of_encript_word=[]
decrypt_word=[]
"""


def clicked():  
    file = filedialog.askopenfilename()
    #lbl.configure(text=res)

window = Tk()
window.columnconfigure(1, weight=1)
#window.font("Helvetica", 16)

window.geometry('800x600')
window.title("Программа шифрования/дешифрования по алгоритму Виженера")



lbl = Label(window, text="Введите текст          ", font=("Helvetica", 12))
lbl.grid(column=2, row=10)

txt = Entry(window,width=50)  
txt.grid(column=5, row=10) 

lbl2 = Label(window, text="Введите ключевое слово", font=("Arial Bold", 12))
lbl2.grid(column=2, row=20)

txt2 = Entry(window,width=20)  
txt2.grid(column=2, row=20) 

btn = Button(window, text="Открыть файл", command=clicked)
btn.grid(column=5, row=30)

txt3 = scrolledtext.ScrolledText(window, width=50,height=5)
txt3.grid(column=5, row=50)

"""
create child window
"""
child_encrypt = Toplevel(window)
child_encrypt.title('Шифруем')
child_encrypt.geometry('800x600')

child_decrypt = Toplevel(window)
child_decrypt.title('Дешифруем')
child_decrypt.geometry('800x600')



"""
menu = Menu(window)
menu.add_command(label='Файл')
window.config(menu=menu)
"""

window.mainloop()


"""
print("Выберите пункт меню. ")


def menu():
        key=input("Для того, чтобы зашифровать текст из файла - нажмите 1, для того, чтобы зашифровать текст при вводе с клавиатуры - нажмите 2 : ")
        if key == "1":
                print("# блок кода, который шифрует текст")
        elif key == "2":
                print("функция, которая шифрует текст при вводе с клавиатуры")
        else:
                key=input("неправильный ввод. Повторить ввод? 1 - да, любая клавиша - нет")
                if key != "1":
                        print("завершение") 
                        #break
                else:
                        print("Единица")
        return key



key=input("Для того, чтобы зашифровать текст - нажмите 1, для того, чтобы расшифровать текст - нажмите 2 : ")
if key == "1":
        print("1111")
        menu()
elif key == "2":
        print("двоечка")
        # блок кода, который расшифровывает текст
else:
        key=input("неправильный ввод. Повторить ввод? 1 - да, любая клавиша - нет")
        if key != "1":
                print("завершение") 
                #break
        else:
                print("Единица")


"""
