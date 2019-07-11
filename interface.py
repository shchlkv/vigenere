#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
#from tkinter import Menu

"""

Здесь указывается, что будет создан класс с именем имя-класса со следующими определениями [def].
Команду __init__(self) проще показать в действии, чем объяснить. __init__() - это конструктор объектов,
позволяющий создавать экземпляр объекта во время исполнения программы.
self - это метка экземпляра, необходимая для привязки переменных класса к данному объекту.
Таким образом инструкция self.master = root создает переменную master и присваивает ей глобальное значение root
[пока еще не определенное]. 
"""


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title ('parent')
        self.master.geometry('400x200')
        self.button = Button(self.master, text = 'myButton')
        self.button.pack(side = TOP)
        #Child()
        self.master.mainloop()

class Child:
    def __init__(self):
        self.slave = Toplevel(root)
        self.slave.title ('child')
        self.slave.geometry('800x600')

root = Tk()

Main(root)
