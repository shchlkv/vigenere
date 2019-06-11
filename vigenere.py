'''
seaching letter of WORD in ALPHABET
get index of letter from ALPHABET

'''

'''
читаем открытый текст из файла, который нужно зашифровать
убрать из него пробелы и знаки препинания и лат.буквы, если есть
+заглавные буквы преобразуем в строчные
зашифровываем и пишем в отдельный файл
vigenere_file_text.txt - исходный файл с текстом
vigenere_file_encrypt.txt - зашифрованный текст
vigenere_file_decrypt.txt - расшифрованный текст

'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys

alphabet=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

#ввести проверку на ввод символов или латиницы

#keyword=list('бетономешалкавйъчыгыхеаюукй')               #password or keyword
#word=list('безинформатикинетникчемноесуществованиеэтогомирабудущегоиникодганебудетмирбслужилямщикоом')
word=[]
indexes_of_keyword=[]           # list, which will to contain indices of keyword
indexes_of_word=[]              # list, which will to contain indices of word
crypt_word=[]
indexes_of_cript_word=[]
decrypt_word=[]

print('your file must to contain text or phrase or word wich you want to encrypt. This file call "vigenere_file_text.txt"')
#word=input('Enter any word or phrase wich need to encrypt. The phrase should be without spaces and with only cyrillic letters: ')
keyword=input('Enter keyword to encrypt the phrase: ')

'''проверка на корректность ввода ключевого слова/фразы

for i in range(len(keyword)):
        if keyword[i] in alphabet:          #cheking of letters from list 'keyword' with index 'i' in list 'alphabet'
                break
        else:
                print('Введены некорректные символы, повторите ввод')
                keyword=input('Enter keyword to encrypt the text/ введите ключевое слово, чтобы зашифровать текст: ')
'''

'''
        1. Проверка наличия введенных символов ключевого слова в списке alphabet
        2. вычисление индексов ключевого слова
        3. индексы букв помещаются в список indexes_of_keyword
        4. проверка на корректность ввода ключевого слова/фразы
        
'''

for i in range(len(keyword)):
       # print(keyword)
        if keyword[i] in alphabet:          #cheking of letters from list 'keyword' with index 'i' in list 'alphabet'
                letter=keyword[i]           #this variable 'letter' contains letter from list 'keyword' with index 'i'. 
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                indexes_of_keyword.append(index_of_letter_from_list_alphabet)  # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 
        else:
                print('Введены некорректные символы, повторите ввод')
                keyword=input('Enter keyword to encrypt the text/ введите ключевое слово, чтобы зашифровать текст: ')
                
''' блок открывает файл vigenere_file_text.txt, читает из него и присваивает переменной word считанный текст '''

vigenere_file_text=open('/home/ark/vigenere_file_text.txt', 'r')
for word in vigenere_file_text:
        word #читаем стороку из файла и присваиваем ее переменной word.
        #Если нет лишних символов, но фраза разбита на строки, то будет зашифрована последняя фраза
        #нужно склеить фразу

'''блок обработки фразы, которую мы будем шифровать'''

word=word.lower() # если в тексте есть заглавные буквы - преобразуем в строчные
word=word.replace(" ", "") #пробелы исключаются
# если нет символа в списке alphabet, то он удаляется.
for letter in word:
        if letter not in alphabet:
                word=word.replace(letter, "")


'''
1. Читаем каждую букву word (то, что считано из файла vigenere_file_text.txt),
2. вычисляем  индекс каждой буквы в списке alhabet,
3. добавляем каждый вычесленный индекс в список indexes_of_word
'''

for i in range(len(word)):
        if word[i] in alphabet:         #it is cheking of letters from list 'word' with index 'i' in list 'alphabet'
                letter=word[i]          #this variable 'letter' is contains letter from list 'word' with index 'i'.
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                indexes_of_word.append(index_of_letter_from_list_alphabet)        # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 


# этот блок шифрует фразу из файла vigenere_file_text.txt 

n=len(word) # количество букв в файле vigenere_file_text.txt
i=0
j=0
while n > 1:
        new_index_letter=(indexes_of_keyword[i]+indexes_of_word[j])%33 # вычисляем индекс зашифрованной буквы
        new_cript_letter=alphabet[new_index_letter] # находим по индексу букву в списке алфавит
        crypt_word.append(new_cript_letter) # добавляем уже зашифрованную букву в конец слова
        n-=1
        i+=1
        j+=1
        if i==len(keyword):
                i=0

#открываем файл
vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'w')
vigenere_file_decrypt=open('/home/ark/vigenere_file_decrypt.txt', 'w')
#пишем в файл vigenere_file_encrypt.txt зашифрованное слово crypt_word
vigenere_file_encrypt.write(''.join(crypt_word)) # список crypt_word надо преобразовать в строковое значение, т.к. списки в файл не записываются
#закрываем файл, в который записали зашифрованное слово                
vigenere_file_encrypt.close() 

#этот блок - активировать, если пользователь захочет вывод на экран
'''
print(''.join(word))
print(''.join(keyword))
print(''.join(crypt_word))
'''

''' БЛОК - РАСШИФРОВКА КАК СЛОВА ИЗ СПИСКА crypt_word, ТАК И ИЗ ФАЙЛА vigenere_file_decrypt.txt '''

#откроем файл на чтение
vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'r')
for word in vigenere_file_encrypt:
        word #читаем стороку из файла и присваиваем ее списку word

print(word)

for i in range(len(word)):
        if crypt_word[i] in alphabet:   
                letter=crypt_word[i]          
                index_of_letter_from_list_alphabet=alphabet.index(letter) 
                indexes_of_cript_word.append(index_of_letter_from_list_alphabet)  # добавляем индекс буквы из списка алфавит в список  indexes_of_cript_word


n=len(word) # количество букв в файле vigenere_file_encrypt.txt
i=0
j=0
while n > 0:
        new_index_letter_decrypt=(indexes_of_cript_word[j]-indexes_of_keyword[i]+33)%33
        new_decript_letter=alphabet[new_index_letter_decrypt]
        decrypt_word.append(new_decript_letter)
        n-=1
        i+=1
        j+=1
        if i==len(keyword):
                i=0
        vigenere_file_decrypt.write(str(new_decript_letter))
                

print(''.join(decrypt_word))
vigenere_file_text.close()
vigenere_file_decrypt.close() 
