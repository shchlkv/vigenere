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


print("Программа предназначена для шифрования и дешифрования текста/фразы/слова по алгоритму Виженера")

def keyword_enter():
        keyword=input('Чтобы зашифровать текст введите ключевое слово, которое должно содержать только буквы кириллического алфавита:  ')
        return keyword.upper()


def keyword_check():
        '''
проверка ввода
'''
        keyword = keyword_enter()
        for letter in keyword:
                if letter not in alphabet:
                        print("Ключевое слово", keyword, " содержит недопустимые символы")
                        break
                else:
                        return keyword

keyword = keyword_check()

for letter in keyword: 
        indexes_of_keyword.append(alphabet.index(letter))  # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 

print('----------------------')
               
'''
блок открывает файл vigenere_file_text.txt,
читает из него текст , трансформирует текст заглавные буквы в строчные,
удаляет пробелы, удаляет символы, которых нет в списке alphabet
'''

with open('/home/ark/vigenere_file_text.txt', 'r') as vigenere_file_text:
        word=vigenere_file_text.read()
        word=word.upper()
        for letter in word:
                if letter not in alphabet:
                        word=word.replace(letter, "")


vigenere_file_text.close()


''' БЛОК ШИФРАЦИИ (фраза из файла vigenere_file_text.txt) '''

def encrypt():
        i = 0
        j = 0
        for letter in word:
                indexes_of_word.append(alphabet.index(letter))
                new_index_letter=(indexes_of_keyword[i]+indexes_of_word[j])%33 # вычисляем индекс зашифрованной буквы
                encrypt_word.append(alphabet[new_index_letter]) # добавляем уже зашифрованную букву в конец слова
                i+=1
                j+=1
                if i==len(keyword):
                        i=0
        return encrypt_word

encrypt_word = encrypt()


#открываем файл
vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'w')
vigenere_file_encrypt.write(''.join(encrypt_word)) # список crypt_word надо преобразовать в строковое значение, т.к. списки в файл не записываются
vigenere_file_encrypt.close() 



''' БЛОК РАСШИФРОВКИ КАК СЛОВА ИЗ СПИСКА encrypt_word, ТАК И ИЗ ФАЙЛА vigenere_file_decrypt.txt '''

#откроем файл на чтение
vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'r')
for word in vigenere_file_encrypt:
        word #читаем стороку из файла и присваиваем ее списку word

       
print(word) #это зашифрованная фраза


def decrypt():
        vigenere_file_decrypt=open('/home/ark/vigenere_file_decrypt.txt', 'w')
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
        vigenere_file_decrypt.write(''.join(decrypt_word))
        print('------------------------------------------------------------------------------')
        print(''.join(decrypt_word))
        vigenere_file_decrypt.close() 
        return decrypt_word


decrypt_word=decrypt()
 

                



