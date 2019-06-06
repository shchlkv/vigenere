'''
эта программа для преобразования текста в файле  в текст, годный к шифровке - без пробелов, заглавных букв, знаков препинания и символов

'''

'''
читаем открытый текст из файла, который нужно зашифровать
убрать из него пробелы и знаки препинания и лат.буквы, если есть
зашифровываем и пишем в отдельный файл
vigenere_file_text.txt - исходный файл с текстом


'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys

alphabet=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')



vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'w')


'''
этот блок открывает файл vigenere_file_text.txt, читает из него и присваивает переменной word считанный текст
'''

vigenere_file_text=open('/home/ark/vigenere_file_text.txt', 'r')
for line in vigenere_file_text:
        word=line #читаем стороку из файла и присваиваем ее списку word


#открываем файл
vigenere_file_decrypt=open('/home/ark/vigenere_file_decrypt.txt', 'w')

vigenere_file_encrypt.write(''.join(crypt_word)) # список crypt_word надо преобразовать в строковое значение, т.к. списки в файл не записываются

vigenere_file_encrypt.close() 


