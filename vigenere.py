'''
seaching letter of WORD in ALPHABET
get index of letter from ALPHABET

'''

'''
читаем открытый текст из файла, который нужно зашифровать
убрать из него пробелы и знаки препинания и лат.буквы, если есть
зашифровываем и пишем в отдельный файл
vigenere_file_text.txt - исходный файл с текстом
vigenere_file_encrypt.txt - зашифрованный файл
vigenere_file_decrypt.txt - расшифрованный файл

'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
alphabet=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
#keyword=list('бетономешалкавйъчыгыхеаюукй')               #password or keyword
#word=list('безинформатикинетникчемноесуществованиеэтогомирабудущегоиникодганебудетмирбслужилямщикоомА')
word=[]
indexes_of_keyword=[]           # list, which will to contain indices of keyword
indexes_of_word=[]              # list, which will to contain indices of word
crypt_word=[]
indexes_of_cript_word=[]
decrypt_word=[]

print('your file must to contain text or phrase or word wich you want to encrypt. This file call "vigenere_file_text.txt"')
#word=input('Enter any word or phrase wich need to encrypt. The phrase should be without spaces and with only cyrillic letters: ')
keyword=input('Enter keyword to encrypt the phrase: ')

vigenere_file_decrypt=open('/home/ark/vigenere_file_decrypt.txt', 'w')
vigenere_file_encrypt=open('/home/ark/vigenere_file_encrypt.txt', 'w')


for i in range(len(keyword)):
        if keyword[i] in alphabet:          #cheking of letters from list 'keyword' with index 'i' in list 'alphabet'
                letter=keyword[i]           #this variable 'letter' contains letter from list 'keyword' with index 'i'. 
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                #print(index_of_letter_from_list_alphabet)
                indexes_of_keyword.append(index_of_letter_from_list_alphabet)  # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 
             
#тут где-то ошибка в строке 52
#надо сделать так: читать строки из файла в список, а дальше работать со списком, как это уже было.
vigenere_file_text=open('/home/ark/vigenere_file_text.txt', 'r')
#print(vigenere_file_text.read(1))
#print(letter)
#for letter in vigenere_file_text:
counter_of_letters_in_text_file=len(letter)
print(len(letter))
        
for i in range(len(word)):
        if word[i] in alphabet:         #cheking of letters from list 'word' with index 'i' in list 'alphabet'
                letter=word[i]          #this variable 'letter' contains letter from list 'word' with index 'i'.
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                indexes_of_word.append(index_of_letter_from_list_alphabet)        # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 

'''
for letter in vigenere_file_text:
        print(letter) #вывод содержимого файла для контроля. выводится построчно
        #print(len(letter)) #кол-во букв в файле
        counter_of_letters_in_text_file=len(letter)
        word=letter
        if letter in alphabet:         #cheking of letters from list 'word' with index 'i' in list 'alphabet'
                #letter=i          #this variable 'letter' contains letter from list 'word' with index 'i'.
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                print(index_of_letter_from_list_alphabet)
                indexes_of_word.append(index_of_letter_from_list_alphabet)        # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 
                print(index_of_letter_from_list_alphabet)
'''
# calculation of cryptword
n=counter_of_letters_in_text_file 
#print(n)
i=0
j=0
while n > 0:
        new_index_letter=(indexes_of_keyword[i]+indexes_of_word[j])%33
        new_cript_letter=alphabet[new_index_letter]
        crypt_word.append(new_cript_letter)
        n-=1
        i+=1
        j+=1
        if i==len(keyword):
                i=0
'''
print(''.join(word))
print(''.join(keyword))
print(''.join(crypt_word))
'''

for i in range(len(word)):
        if crypt_word[i] in alphabet:         
                letter=crypt_word[i]          
                index_of_letter_from_list_alphabet=alphabet.index(letter) 
                indexes_of_cript_word.append(index_of_letter_from_list_alphabet)  

n=counter_of_letters_in_text_file
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

'''
print('Расшифрованное слово: ')
print(''.join(decrypt_word))
'''
vigenere_file_text.close()
vigenere_file_encrypt.close()
vigenere_file_decrypt.close() 
