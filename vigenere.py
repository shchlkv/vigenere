"""
Программа предназначена для шифрования и дешифрования текста/фразы/слова по алгоритму Виженера
        1. Проверка наличия введенных символов ключевого слова в списке alphabet
        2. вычисление индексов ключевого слова
        3. индексы букв помещаются в список indexes_of_keyword
        4. проверка на корректность ввода ключевого слова/фразы
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys

alphabet=list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
word=[]
indexes_of_keyword=[]         
indexes_of_word=[]            
encrypt_word=[]
indexes_of_encript_word=[]
decrypt_word=[]


def keyword_enter():
        '''
ввод проверка ключевого слова на недопустимые символы
'''
        keyword = input('Чтобы зашифровать текст введите ключевое слово, которое должно содержать только буквы кириллического алфавита:  ')
        return keyword.upper()
        for letter in keyword:
                if letter not in alphabet:
                        print("Ключевое слово", keyword,  "содержит недопустимые символы")
                        break
                else:
                        return keyword


def keyword_indexes():
        '''
вычисление индексов ключевого слова
'''
        for letter in keyword: 
                indexes_of_keyword.append(alphabet.index(letter))  # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword'
        return indexes_of_keyword
               

def clear_text():
        '''
блок открывает файл vigenere_file_text.txt,
читает из него текст , трансформирует текст: строчные в заглавные буквы,
удаляет пробелы, удаляет символы, которых нет в списке alphabet
'''
        with open('/home/ark/vigenere_file_text.txt', 'r') as vigenere_file_text:
                word=vigenere_file_text.read()
                word=word.upper()
                for letter in word:
                        if letter not in alphabet:
                                word=word.replace(letter, "")
        return word

                #################
                # БЛОК ШИФРОВКИ #
                #################

def encrypt():
        '''
БЛОК ШИФРАЦИИ (шифруем фразу из файла vigenere_file_text.txt) '''        
        i = 0
        j = 0
        for letter in clear_text:
                indexes_of_word.append(alphabet.index(letter)) #вычислаяем индекс буквы из текста
                new_index_letter=(indexes_of_keyword[i]+indexes_of_word[j])%33 # вычисляем индекс зашифрованной буквы
                encrypt_word.append(alphabet[new_index_letter]) # добавляем уже зашифрованную букву в конец 
                i+=1
                j+=1
                if i==len(keyword):
                        i=0
        return encrypt_word

with open('/home/ark/vigenere_file_encrypt.txt', 'w') as vigenere_file_encrypt:
        keyword = keyword_enter()
        indexes_of_keyword=keyword_indexes()
        clear_text=clear_text()
        encrypt()
        vigenere_file_encrypt.write(''.join(encrypt_word)) # список crypt_word надо преобразовать в строковое значение, т.к. списки в файл не записываются


##################################################################
# БЛОК РАСШИФРОВКИ ТЕКСТА ИЗ ФАЙЛА vigenere_file_decrypt.txt     #
##################################################################


"""
1. открываем файл с зашифрованным текстом
2. считываем текст и закрываем файл
3. расшифровываем
4. открываем файл для расшифрованного текста, пишем в него и закрываем

"""

def decrypt():
        i = 0
        j = 0
        for letter in word:
                indexes_of_encript_word.append(alphabet.index(letter))
                new_index_letter_decrypt=(indexes_of_encript_word[j]-indexes_of_keyword[i]+33)%33
                decrypt_word.append(alphabet[new_index_letter_decrypt])
                i+=1
                j+=1
                if i == len(keyword):
                        i = 0
                #vigenere_file_decrypt.write(str(new_decript_letter))
        return decrypt_word


with open('/home/ark/vigenere_file_encrypt.txt', 'r') as vigenere_file_encrypt:
        word=vigenere_file_encrypt.read()
        print(word)

print('------------------------------------------------------------------------------')

with open('/home/ark/vigenere_file_decrypt.txt', 'w') as vigenere_file_decrypt:
        decrypt()
        vigenere_file_decrypt.write(''.join(decrypt_word))
        print(''.join(decrypt_word))
